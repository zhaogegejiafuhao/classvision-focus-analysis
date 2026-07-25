# ClassVision 课堂注意力智能分析系统

融合视线、头部姿态与疲劳特征的 Web 端课堂专注度量化平台，集成 AI 组卷、智能批改、RAG 知识库、在线判题等教学场景。

## 📌 项目简介

ClassVision 是一个面向教育教学场景的全栈智能平台，从课堂注意力分析出发，逐步扩展为覆盖教学全流程的 AI 辅助系统：

1. **课堂注意力分析** — WebRTC 无插件采集摄像头，YOLOv8+ByteTrack 多人跟踪，MediaPipe 468 关键点，融合视线/俯仰/眨眼计算 0-100 注意力指数
2. **AI 智能组卷** — LLM 驱动的自动出题 + 渐进式换题匹配 + 模板化试卷生成
3. **智能批改与审核** — OCR 答题卡识别 + LLM 评分 + 教师审核工作流 + 批量确认
4. **RAG 知识库** — 文档上传、混合检索（BM25+FAISS）、HyDE 改写、对话式问答
5. **在线判题 (OJ)** — Docker 沙箱判题，支持 Python/C/Java 等多语言
6. **教学管理** — 作业、签到、请假、通知、错题本、知识点雷达、成绩报告

## ✨ 核心功能

| 模块 | 功能 |
|------|------|
| 注意力分析 | 实时摄像头/视频回放 · 多人独立跟踪 · 低头/侧视/疲劳识别 · 注意力曲线 · AI 课堂总结 |
| AI 组卷 | LLM 自动出题 · 题库检索组卷 · 渐进式换题 · 试卷模板 · 难度分布分析 |
| 智能批改 | 答题卡 OCR · 选择题/填空题/简答题 AI 评分 · 教师审核工作流 · 批量确认 · 导出报告 |
| RAG 知识库 | 文档上传(PDF/Word/PPT) · 混合检索 · HyDE 改写 · Cross-Encoder 重排 · 对话历史 |
| 在线判题 | 多语言支持 · Docker 沙箱 · 实时输出 · 提交记录 |
| 教学管理 | 作业收发 · 签到打卡 · 请假审批 · 通知系统 · 错题本 · 知识点分析 · 成绩报告 |

## 🛠️ 技术栈

| 层级 | 技术 |
|------|------|
| 前端 | Vue 3 + Vite + Ant Design Vue + ECharts + WebSocket |
| 后端 | FastAPI + Uvicorn + SQLAlchemy + SQLite |
| CV 引擎 | OpenCV + YOLOv8 + MediaPipe + InsightFace + ONNX Runtime |
| AI/LLM | Ollama (qwen3:4b) / SiliconFlow / 火山引擎豆包 |
| RAG | sentence-transformers + FAISS + BM25 + bge-reranker |
| 判题 | Docker 沙箱 + 子进程隔离 |

## 📁 项目结构

```
ClassVision/
├── backend/               # FastAPI 后端
│   ├── api/               # 路由层（按功能域拆分）
│   ├── core/              # 配置、数据库、安全
│   ├── models/            # SQLAlchemy 模型 & Pydantic Schema
│   ├── services/          # 业务逻辑（批改、OCR、评分等）
│   ├── seed_data.py       # 测试数据填充
│   └── import_tal_scq5k.py # TAL-SCQ5K 题库导入
├── frontend/              # Vue 3 前端
│   └── src/
│       ├── api/           # API 调用层
│       ├── components/    # 组件（ai-grading, answer-sheet, exam-compose 等）
│       ├── composables/   # 组合式函数
│       ├── stores/        # Pinia 状态管理
│       └── views/         # 页面视图
├── cv_engine/             # CV 视觉引擎
│   ├── analyzers/         # 注意力、疲劳、姿态分析
│   ├── detectors/         # 人脸检测、答题卡检测
│   └── trackers/          # 人脸跟踪
├── rag/                   # RAG 检索模块
├── oj/                    # 在线判题（Docker 子模块）
├── data/                  # 数据目录（题库、RAG 索引、知识文档）
├── models/                # 模型文件（YOLOv8、InsightFace）
├── tests/                 # 正式测试套件
├── scripts/               # 开发辅助脚本
└── .githooks/             # Git pre-commit hooks
```

## ⚙️ 环境要求

- Python 3.11+
- Node.js 18+
- Ollama（本地 LLM）或云端 API Key
- 内存推荐 8GB+，CPU 可完整运行无需独显
- Docker（可选，用于 OJ 判题）

## 🚀 快速开始

```bash
# 1. 克隆项目
git clone https://github.com/zhaogegejiafuhao/classvision-focus-analysis.git
cd ClassVision

# 2. 创建虚拟环境并安装依赖
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate    # Linux/Mac
pip install -r requirements.txt

# 3. 安装前端依赖
cd frontend && npm install && cd ..

# 4. 配置环境变量
cp .env.example .env
# 编辑 .env 填入 API Key（或使用 Ollama 本地模型）

# 5. 初始化数据库（首次运行）
set PYTHONPATH=D:\ClassVision
.venv\Scripts\python -m backend.seed_data

# 6. 启动后端
.venv\Scripts\python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload

# 7. 启动前端（新终端）
cd frontend && npm run dev

# 8. 访问 http://localhost:5173
```

### 测试账号

| 角色 | 用户名 | 密码 |
|------|--------|------|
| 管理员 | admin | 123456 |
| 教师 | teacher | teacher123 |
| 学生 | student | student123 |

## 🔒 Git Hooks

项目配置了 pre-commit hooks，防止意外提交：
- 禁止提交 `.env`、`.db`、`.pyc`、`.log` 等文件
- 禁止提交 `__pycache__`
- 大文件（>5MB）警告
- API 密钥泄露检测

克隆后需设置 hooks 路径：
```bash
git config core.hooksPath .githooks
```

## 📄 License

MIT License
