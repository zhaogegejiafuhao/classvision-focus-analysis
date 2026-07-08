# ClassVision课堂注意力智能分析系统｜完整项目说明书（含Git仓库规范）

# 一、项目整体概述

## 1\.1 项目名称

**中文全称**：融合视线与姿态特征的课堂注意力智能分析系统

**项目简称**：ClassVision 课眼智析

## 1\.2 项目背景与痛点

传统线下课堂、线上会议缺乏**量化、无感知、自动化**的听众专注度评估手段。教师仅能主观判断课堂状态，无法获取：

- 每位学生实时注意力分数

- 课堂分心高发时间段

- 低头、转头、疲劳犯困等行为统计

- 整堂课标准化教学分析报告

本项目基于计算机视觉 \+ Web流媒体 \+ 本地大模型，实现**无感知、全自动、端到端**的课堂注意力分析系统，解决传统课堂无法量化评估的行业痛点。

## 1\.3 项目核心亮点（区别于普通实训项目）

- 非烂大街CRUD系统，属于**AI视觉\+流媒体\+大模型融合项目**，全校重复率极低

- 底层视觉推理 \+ 后端工程 \+ 前端可视化 \+ AI报告**全覆盖**，三人分工绝对均衡

- 完全**离线本地运行**（Ollama本地大模型），无需联网、无需付费API

- 自研**多特征融合注意力打分算法**，并非单纯图像识别

- 支持**实时摄像头 \+ 本地视频回放**双模式

---

# 二、系统整体架构（四层解耦架构）

本项目采用**前端流媒体层 → 后端服务层 → CV算法推理层 → AI大模型分析层**四层架构，完全解耦，适合团队协作开发。

## 2\.1 前端交互与流媒体层（同学A）

负责视频采集、实时推流、画面渲染、数据可视化、报表展示。

**核心能力**：浏览器无插件实时视频采集，WebSocket实时帧传输，Canvas实时绘制人脸框、关键点、行为标签，ECharts注意力曲线展示。

## 2\.2 后端服务与数据持久层（同学B）

基于FastAPI异步架构，负责WebSocket长连接流媒体转发、视频帧缓冲、数据库时序存储、用户课堂管理、Ollama大模型接口封装。

## 2\.3 计算机视觉推理层（同学C）

系统核心智能层：YOLOv8多人检测 \+ ByteTrack多目标跟踪 \+ MediaPipe人脸468关键点解析，计算头部姿态、视线偏移、眨眼疲劳度，输出0\~100注意力指数。

## 2\.4 本地大模型分析层（全局模块）

接收视觉层输出的结构化统计数据，通过Qwen2\.5\-7B本地大模型自动生成**课堂评价、问题总结、教学改进建议**。

**注意：本项目不使用视觉多模态模型，采用“视觉感知\+文本推理”解耦架构，性能更高、更稳定。**

---

# 三、最终定型完整技术栈（100%适配实训）

## 3\.1 前端技术栈（Vue3 组）

- 框架：Vue3 \+ Vite

- UI组件：Ant Design Vue

- 流媒体：WebSocket实时帧传输 + 浏览器原生摄像头API（getUserMedia）

- 画面渲染：Canvas

- 数据可视化：ECharts

- 通信：WebSocket \+ Axios

## 3\.2 后端技术栈（FastAPI 组）

- 服务框架：FastAPI（异步高性能）

- 运行服务：Uvicorn

- 数据库：SQLite（轻量零配置，适配时序数据统计）

- ORM：SQLAlchemy

- 大模型调用：ollama\-python

## 3\.3 视觉算法技术栈（CV组）

- 图像处理：OpenCV、NumPy

- 多人脸检测：YOLOv8\-Face

- 多目标跟踪：ByteTrack

- 人脸关键点与姿态：MediaPipe FaceMesh（468关键点）

- 自研算法：注意力多特征加权融合算法

## 3\.4 AI大模型最终选型

- 模型：**qwen2\.5:7b\-q4\_K\_M**

- 部署方式：Ollama本地离线部署

- 选择理由：中文最强、体积小、CPU可跑、128K长上下文、适合生成教学报告

- **不采用VL多模态模型**：项目已完成视觉结构化提取，无需重复图像推理，降低设备压力

---

# 四、系统核心功能清单（最终版）

1. **双视频源接入**：浏览器实时摄像头、本地MP4视频文件上传分析

2. **多人脸实时跟踪**：自动分配ID，稳定区分每一位学生

3. **多维度行为分析**：低头/抬头/左右转头、视线偏移、眨眼疲劳检测

4. **注意力指数量化**：视线40% \+ 姿态35% \+ 疲劳25% 加权计算 0\~100分数

5. **实时画面渲染**：前端Canvas绘制人脸框、关键点、行为标签、注意力分数

6. **课堂数据统计可视化**：注意力曲线、行为占比饼图、时段分析图

7. **AI自动课堂报告生成**：整体评价、问题总结、教学改进建议

8. **历史课堂数据存储与查询**

9. **分析报告预览与导出**

---

# 五、三人详细分工（最终定稿，可直接上交）

## 5\.1 同学A：前端 \+ 流媒体可视化开发

- Vue3项目搭建、页面布局、UI组件开发

- 摄像头采集（getUserMedia）、视频文件上传预览

- WebSocket前后端实时通信封装

- Canvas实时绘制检测框、人脸关键点、行为标签

- ECharts图表实现注意力时序曲线、行为统计看板

- 历史记录页面、AI报告展示、PDF导出功能

## 5\.2 同学B：后端服务 \+ 数据库 \+ AI接口

- FastAPI项目分层架构搭建（路由/服务/模型）

- WebSocket视频帧转发、帧缓冲、降帧优化

- SQLite数据表设计、时序行为数据存储

- 用户、课堂、历史记录全套业务接口

- Ollama模型调用封装，接收统计数据生成报告并入库

- 跨域、日志、异常处理、前后端联调

## 5\.3 同学C：CV视觉算法 \+ 注意力评分 \+ 数据聚合

- YOLOv8\-face \+ ByteTrack多人脸跟踪搭建

- MediaPipe 468关键点提取、头部姿态解算（Pitch/Yaw）

- EAR眼部比值计算，实现眨眼、疲劳判定

- 自研注意力加权打分算法实现与调参

- 课堂行为数据统计、指标聚合、结构化输出

- 算法帧率优化、防抖、异常画面容错处理

---

# 六、GitHub 仓库完整配置方案（可直接新建）

## 6\.1 仓库基础信息

- **仓库名称**：classvision\-focus\-analysis

- **仓库简介**：Web端课堂/会议多目标注意力视觉分析系统，基于YOLOv8\+MediaPipe实现多人姿态、视线、疲劳检测，FastAPI\+Vue3流媒体实时传输，Ollama本地Qwen2\.5生成课堂分析报告。

- **可见性**：Private（实训防查重）

- **初始化勾选**：README、Python \.gitignore、MIT License

- **仓库标签Topics**：computer\-vision、yolov8、mediapipe、fastapi、vue3、ollama、attention\-detection

## 6\.2 标准目录结构（最终规范）

```Plain Text
classvision-focus-analysis/
├── frontend/          # Vue3前端工程
├── backend/          # FastAPI后端服务
├── cv_engine/        # 视觉推理核心算法
├── docs/             # 实训报告、架构图、数据库文档
├── .gitignore        # 项目忽略文件
├── README.md         # 项目主页介绍
└── requirements.txt  # Python依赖

```

## 6\.3 可直接使用的 \.gitignore 补充规则

```Plain Text
# 模型与缓存
*.bin
*.gguf
ollama_cache/

# 媒体文件
*.mp4
*.avi
video_upload/
output/

# 项目缓存
__pycache__/
*.pyc
.idea/
.vscode/
node_modules/
dist/

```

## 6\.4 团队协作配置

- 仓库创建者创建私有仓库

- Settings \-\> Collaborators 添加两位组员

- 权限设置为 Write（可提交代码）

---

# 七、所有开源依赖仓库地址（答辩可直接引用）

本项目**无完整开源成品抄袭**，仅复用底层组件，业务逻辑全自研，绝对安全不查重。

## 7\.1 CV算法依赖仓库（同学C）

- YOLOv8 官方：https://github.com/ultralytics/ultralytics

- ByteTrack 多目标跟踪：https://github.com/FoundationVision/ByteTrack

- MediaPipe 官方：https://github.com/google/mediapipe

- 头部姿态估计参考：https://github.com/shenasa-ai/head-pose-estimation

- 疲劳检测（EAR眨眼）参考：https://github.com/imprvhub/somnolence-detection

## 7\.2 后端FastAPI依赖仓库（同学B）

- FastAPI 官方框架（内置WebSocket支持，官方文档含视频流示例）：https://github.com/fastapi/fastapi

- ollama-python SDK：https://github.com/ollama/ollama-python

- FastAPI 全栈模板（PostgreSQL+SQLAlchemy，官方维护新版）：https://github.com/fastapi/full-stack-fastapi-template

## 7\.3 前端Vue可视化依赖仓库（同学A）

- Vue3 ECharts官方组件 vue-echarts：https://github.com/ecomfe/vue-echarts

- 摄像头采集：浏览器原生API（navigator.mediaDevices.getUserMedia），参考MDN文档 https://developer.mozilla.org/zh-CN/docs/Web/API/MediaDevices/getUserMedia

---

# 八、项目优势与答辩话术总结（可直接复制论文）

1. **技术新颖性高**：融合Web流媒体、多目标视觉检测、姿态视线分析、本地大模型文本生成，区别于传统管理系统。

2. **架构解耦清晰**：感知层、服务层、AI推理层分层明确，工程化规范。

3. **自研程度高**：仅复用底层开源组件，多人匹配逻辑、注意力融合算法、全链路业务逻辑均为本组独立开发。

4. **部署门槛低**：全CPU离线运行，无需服务器、无需GPU、无需联网。

5. **工作量均衡**：三人分别负责前端流媒体、后端工程、AI视觉算法，无划水、无超负荷。

---

# 九、可选拓展功能（加分项，有余力开发）

可在报告“未来展望/系统拓展”写入：

1. **接入RAG教学知识库**，上传教案、课件，让AI结合课程内容生成更精准的教学建议，进一步提升项目深度。

2. **升级WebRTC低延迟传输**，当前采用WebSocket传输视频帧，未来可引入WebRTC（aiortc: https://github.com/aiortc/aiortc）实现P2P低延迟流媒体传输，降低带宽占用、提升实时性。

> （注：部分内容可能由 AI 生成）
