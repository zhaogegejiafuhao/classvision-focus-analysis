# ClassVision 课堂注意力智能分析系统
融合视线、头部姿态与疲劳特征的Web端课堂/会议专注度量化平台

## 📌 项目简介
针对线下课堂、线上会议无法量化听众专注度痛点，搭建端到端视觉分析平台：
1. WebRTC浏览器无插件采集实时摄像头/本地视频文件
2. YOLOv8+ByteTrack多人人脸跟踪，MediaPipe提取468关键点
3. 融合视线偏移、俯仰角度、眨眼频率计算0-100注意力指数
4. FastAPI WebSocket实时传输视频帧与识别结果，SQLite存储时序行为数据
5. Ollama本地部署qwen3:4b离线大模型，自动生成结构化课堂教学改进报告

## ✨ 核心功能
- 双视频源：实时摄像头、本地MP4视频上传回放
- 多目标跟踪：独立ID区分每位听众，单人独立注意力打分
- 行为识别：低头、侧视、疲劳犯困量化统计
- 可视化看板：ECharts实时注意力曲线、课堂行为分布报表
- AI自动分析：离线生成课堂总结、分心问题、教学优化建议
- 历史课堂记录存储、报表导出

## 🛠️ 完整技术栈
### 前端（Vue3）
Vue3 + Vite + Ant Design Vue | WebRTC | Canvas | ECharts | WebSocket
### 后端（Python）
FastAPI | Uvicorn | SQLite | SQLAlchemy | ollama-python
### 计算机视觉算法
OpenCV | NumPy | YOLOv8-face | ByteTrack | MediaPipe FaceMesh
### 本地大模型
qwen3:4b

## ⚙️ 环境部署要求
1. Python >= 3.10
2. Node.js >= 18
3. Ollama 客户端
4. 内存推荐8G及以上，CPU可完整运行无需独显