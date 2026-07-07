# 修复 mediapipe 0.10.35 兼容性 & 验证全链路启动

## 摘要

mediapipe 0.10.35（Windows 专用版）没有 `mp.solutions` API，只有 `mp.tasks` API。
`pose_estimator.py` 和 `fatigue_detector.py` 使用了不存在的 `mp.solutions.face_mesh`，
导致后端启动时 `AttentionAnalyzer()` 初始化失败 (`AttributeError`)。

本计划将这两个文件改用 `mediapipe.tasks.python.vision.FaceLandmarker` API 重写，
下载对应的 `.task` 模型文件，并验证全链路启动。

## 当前状态分析

- **mediapipe 版本**: 0.10.35，仅有 `mp.tasks`，无 `mp.solutions`
- **可用 API**: `FaceLandmarker`, `FaceLandmarkerOptions`, `FaceLandmarkerResult`
- **FaceLandmarkerResult 结构**:
  - `face_landmarks: List[List[NormalizedLandmark]]` — 每张脸 468 个关键点
  - `face_blendshapes: List[List[Category]]` — 可选表情系数
  - `facial_transformation_matrixes: List[np.ndarray]` — 可选人脸变换矩阵
- **模型文件**: 需要 `face_landmarker.task`，当前项目内不存在
- **参考仓库**: 两个参考仓库也使用 `mp.solutions`，同样不兼容 0.10.35
- **requirements.txt**: `mediapipe>=0.10.9`，psycopg2-binary 已不需要（改用 SQLite）

## 修改计划

### 1. 下载 face_landmarker.task 模型文件

- **文件**: `d:\ClassVision\cv_engine\models\face_landmarker.task`
- **来源**: Google 官方 `https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/latest/face_landmarker.task`
- **方式**: 用 Python `urllib` 下载，约 1.5MB
- 如果下载失败，提供手动下载指引

### 2. 重写 `d:\ClassVision\cv_engine\analyzers\pose_estimator.py`

核心变化:
- `mp.solutions.face_mesh.FaceMesh` → `FaceLandmarker` (tasks API)
- `face_mesh.process(rgb)` → `landmarker.detect(mp_image)` where `mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)`
- `results.multi_face_landmarks[0].landmark` → `result.face_landmarks[0]` (list of NormalizedLandmark)
- 关键点索引保持不变（鼻尖1, 下巴152, 左眼33, 右眼263, 左嘴61, 右嘴291）
- solvePnP 逻辑不变
- 添加懒加载模式：模型文件不存在时不崩溃，返回默认值

### 3. 重写 `d:\ClassVision\cv_engine\analyzers\fatigue_detector.py`

核心变化:
- 同样从 `mp.solutions.face_mesh` 迁移到 `FaceLandmarker`
- EAR 计算逻辑不变，关键点索引不变
- 可以复用同一个 FaceLandmarker 实例（通过参数传入），避免重复加载模型

### 4. 优化 `d:\ClassVision\cv_engine\analyzers\attention_analyzer.py`

- PoseEstimator 和 FatigueDetector 共享一个 FaceLandmarker 实例
- 在 AttentionAnalyzer 中创建 FaceLandmarker，传给两个子分析器
- 这样每帧只需做一次人脸关键点检测，性能翻倍

### 5. 更新 `d:\ClassVision\requirements.txt`

- 移除 `psycopg2-binary==2.9.10`（已改用 SQLite）
- 确认 mediapipe 版本约束合适

### 6. 验证全链路

- 运行 `from backend.main import app` 确认无导入错误
- 运行 `uvicorn backend.main:app --reload` 确认服务启动
- 运行 `npm run dev` 确认前端启动

## 详细代码设计

### pose_estimator.py 重写方案

```python
import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks.python.vision import FaceLandmarker

class PoseEstimator:
    MODEL_PATH = "cv_engine/models/face_landmarker.task"

    def __init__(self, landmarker: FaceLandmarker = None):
        self._landmarker = landmarker
        self._owns_landmarker = landmarker is None
        self.model_points = np.array([...])  # 不变

    @property
    def landmarker(self):
        if self._landmarker is None:
            options = mp.tasks.python.vision.FaceLandmarkerOptions(
                base_options=mp.tasks.python.BaseOptions(model_asset_path=self.MODEL_PATH),
                running_mode=mp.tasks.python.vision.RunningMode.IMAGE,
                num_faces=1,
            )
            self._landmarker = FaceLandmarker.create_from_options(options)
        return self._landmarker

    def estimate(self, frame, bbox):
        # 裁剪人脸区域
        # 转 RGB, 创建 mp.Image
        # landmarker.detect(mp_image)
        # 从 result.face_landmarks[0] 取关键点
        # solvePnP 计算角度（逻辑不变）
```

### fatigue_detector.py 重写方案

```python
import numpy as np
from mediapipe.tasks.python.vision import FaceLandmarker, FaceLandmarkerResult

class FatigueDetector:
    LEFT_EYE = [33, 160, 158, 133, 153, 144]
    RIGHT_EYE = [362, 385, 387, 263, 373, 380]

    def __init__(self, landmarker: FaceLandmarker = None):
        self._landmarker = landmarker  # 共享 landmarker
        # ...

    def detect(self, frame, bbox, landmarker_result: FaceLandmarkerResult = None):
        # 如果传入了 landmarker_result，直接用
        # 否则自己调用 landmarker.detect()
        # EAR 计算（逻辑不变）
```

### attention_analyzer.py 优化方案

```python
class AttentionAnalyzer:
    def __init__(self):
        # 创建共享 FaceLandmarker
        self._landmarker = None
        self.pose_estimator = PoseEstimator(landmarker=self._get_landmarker())
        self.fatigue_detector = FatigueDetector(landmarker=self._get_landmarker())

    def _get_landmarker(self):
        # 懒加载共享 landmarker
```

或者更简洁：让 PoseEstimator 和 FatigueDetector 各自独立创建 landmarker（因为 IMAGE 模式下每次 detect 是独立的），但这样性能差一些。

**最终方案**: 在 AttentionAnalyzer 中共享 FaceLandmarker，每帧只调用一次 detect，把 result 传给两个子分析器。

## 假设与决策

1. **运行模式**: 使用 `IMAGE` 模式（逐帧 detect），不用 `VIDEO` 模式（需要 timestamp_ms）或 `LIVE_STREAM` 模式（异步回调更复杂）
2. **共享 landmarker**: PoseEstimator 和 FatigueDetector 共享一个 FaceLandmarker 实例，每帧只做一次人脸关键点检测
3. **模型文件路径**: 硬编码为 `cv_engine/models/face_landmarker.task`，支持通过环境变量覆盖
4. **降级策略**: 模型文件不存在时，pose_estimator 和 fatigue_detector 返回默认值，不影响整体流程
5. **关键点索引**: 与 `mp.solutions.face_mesh` 的 468 点索引完全一致，无需修改

## 验证步骤

1. 确认 `face_landmarker.task` 模型文件已下载
2. 确认 `d:\ClassVision\.venv\Scripts\python.exe -c "from cv_engine.analyzers.attention_analyzer import AttentionAnalyzer; print('OK')"` 无报错
3. 确认 `d:\ClassVision\.venv\Scripts\python.exe -c "from backend.main import app; print('OK')"` 无报错
4. 确认 `uvicorn backend.main:app --reload` 启动成功
5. 确认前端 `npm run dev` 启动成功
