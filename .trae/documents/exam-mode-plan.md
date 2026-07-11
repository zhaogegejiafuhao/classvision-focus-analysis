# 模块1：考场专用注意力识别 实现计划

## Context

当前 ClassVision 的注意力分析是单帧独立评分（视线40% + 姿态35% + 疲劳25%），没有时序概念。考场场景需要跨帧累积时长、计数事件、综合判别风险等级，同时新增"考场模式"开关让普通课堂和考场共用一套代码。

## 改动总览

| 文件 | 操作 | 说明 |
|------|------|------|
| `cv_engine/utils/__init__.py` | 新建 | 空文件，声明包 |
| `cv_engine/utils/time_state_machine.py` | 新建 | 时序状态机核心 |
| `cv_engine/analyzers/attention_analyzer.py` | 修改 | 集成考场模式 |
| `backend/models/tables.py` | 修改 | Classroom.exam_mode + ExamRiskRecord 表 |
| `backend/core/database.py` | 修改 | 新增迁移函数 |
| `backend/models/schemas.py` | 修改 | 新增/扩展字段 |
| `backend/api/routes.py` | 修改 | 按模式切换 analyzer，保存风险记录 |
| `backend/api/classroom_routes.py` | 修改 | 支持 exam_mode，修复 records 未定义 bug |
| `backend/api/stats_routes.py` | 修改 | 学生列表返回风险等级 |
| `frontend/src/views/HomePage.vue` | 修改 | 表单加考场模式开关 |
| `frontend/src/views/LivePage.vue` | 修改 | 风险看板 + 高风险 Alert + 风险标签绘制 |
| `frontend/src/views/ClassroomDetail.vue` | 修改 | 风险分布图 + 学生列表风险列 |

## 实现步骤

### 阶段1：时序状态机（新建文件）

**`cv_engine/utils/__init__.py`** — 空文件

**`cv_engine/utils/time_state_machine.py`** — 核心数据结构：

- `RiskLevel` 枚举：LOW / MEDIUM / HIGH
- `PersonExamState` 数据类：每个 track_id 的状态
  - `gaze_deviation_start` / `head_down_start` — 连续异常起始时刻（monotonic）
  - `head_turn_events` — 转头事件次数（边沿触发：normal→deviant 算一次）
  - 阈值：YAW=15°, PITCH=20°, SUSTAINED=2s, TURN_MEDIUM=5, TURN_HIGH=10
- `ExamStateMachine` 类：
  - `update(track_id, pitch, yaw, fatigue, cheating_nearby)` → 返回风险结果 dict
  - `cleanup(active_ids)` — 清除消失的 track_id
  - `_compute_risk(state)` — 风险等级判定：
    - HIGH：偏视≥2s / 低头≥2s且附近有作弊物品 / 转头≥10次
    - MEDIUM：偏视≥1s / 低头≥1s / 转头≥5次 / 附近有作弊物品
    - LOW：其余

使用 `time.monotonic()` 避免系统时钟调整影响。

### 阶段2：CV 引擎集成

**`attention_analyzer.py`** 修改：

1. 导入 `ExamStateMachine`
2. `__init__(exam_mode=False)` 新增参数，考场模式时创建 `self._exam_sm`
3. 考场模式权重：GAZE=0.50, POSE=0.35, FATIGUE=0.15（偏视权重更高）
4. `analyze(frame, tracked_faces, objects=None)` 新增可选 objects 参数
5. 考场模式：调用 `_score_gaze_exam()`（yaw * 3.5 更严格）、调用状态机、附加 `exam_risk` 字段
6. 新增 `_check_cheating_nearby(bbox, objects)` — 判断作弊物品 bbox 是否在人物 150px 内
7. 末尾清理状态机和 blink_states

### 阶段3：数据库层

**`tables.py`**：
- `Classroom` 新增 `exam_mode: Mapped[bool]`
- 新增 `ExamRiskRecord` 表：student_id, classroom_id, timestamp, risk_level, gaze_deviation_duration, head_down_duration, head_turn_events, cheating_object_nearby, attention_score
- Student / Classroom 新增反向关系

**`database.py`**：
- `init_db()` 追加 `_migrate_classroom_exam_mode()`

**`schemas.py`**：
- `ClassroomCreate` 加 `exam_mode: bool = False`
- `ClassroomOut` 加 `exam_mode: bool = False`
- `StudentOut` 加 `risk_level: str | None = None`

### 阶段4：后端路由

**`routes.py`**：
- `_analyzers: dict[int, AttentionAnalyzer]` 按 classroom_id 缓存
- `_get_analyzer(classroom_id, exam_mode)` 获取/创建对应模式的 analyzer
- `_process_frame(frame, classroom_id, exam_mode)` 传入 objects
- `_save_records(classroom_id, faces, exam_mode)` 考场模式额外保存 ExamRiskRecord
- WebSocket 连接时查询 classroom.exam_mode，断连时清理 analyzer 缓存

**`classroom_routes.py`**：
- `create_classroom` 支持 exam_mode
- `get_classroom` 修复 `records` 未定义 bug（第42行），考场模式追加 risk_distribution
- `end_classroom` 不变

**`stats_routes.py`**：
- `get_students` 考场模式查询最新 ExamRiskRecord 返回 risk_level

### 阶段5：前端

**`HomePage.vue`**：
- 表单加 `a-switch` 控件 `exam_mode`
- `form.ref` 追加 `exam_mode: false`

**`LivePage.vue`**：
- onMounted 获取 classroom 信息，设 `isExamMode`
- WebSocket 返回数据含 `exam_mode` 字段
- 考场模式看板：低/中/高风险人数统计
- `drawResults()` 考场模式按风险等级绘制边框颜色和标签（绿/橙/红）
- 高风险 Alert 弹窗，5秒自动关闭，`lastAlertTime` 防闪烁

**`ClassroomDetail.vue`**：
- 考场模式：风险分布饼图替代注意力趋势图
- 学生列表追加风险等级列（a-tag 彩色标签）

## 顺带修复的 Bug

`classroom_routes.py:42` 引用了未定义的 `records` 变量。需在第34行前增加 `records = db.query(AttentionRecord).filter(...).all()`。

## 验证方案

1. 启动后端，确认 `_migrate_classroom_exam_mode()` 成功执行
2. 创建普通课堂和考场模式课堂，确认 exam_mode 字段正确
3. 打开考场模式课堂的 LivePage，摄像头前偏头 2 秒以上，确认风险等级变为 HIGH
4. 确认高风险 Alert 弹窗出现并 5 秒后消失
5. 结束课堂，打开 ClassroomDetail，确认风险分布饼图和学生列表风险列正确显示
6. 创建普通课堂，确认原有功能不受影响（无 exam_risk 字段）
