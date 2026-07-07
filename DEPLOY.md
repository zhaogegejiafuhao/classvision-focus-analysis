# ClassVision 部署指南

## 一、一键部署（推荐）

### Windows 用户

1. **下载项目**
   ```bash
   git clone https://github.com/zhaogegejiafuhao/classvision-focus-analysis.git
   cd classvision-focus-analysis
   ```

2. **右键运行 `deploy.ps1`**
   - 右键点击 `deploy.ps1` → 选择"使用 PowerShell 运行"
   - 或在 PowerShell 中执行：`.\deploy.ps1`

3. **等待自动安装**
   - 脚本会自动检查并安装：
     - Python 3.11
     - Node.js 20 LTS
     - Ollama + qwen3:4b 模型（约 2.5GB）
     - MediaPipe FaceLandmarker 模型
     - 所有 pip 和 npm 依赖

4. **自动启动**
   - 安装完成后会自动启动前后端服务
   - 浏览器会自动打开 http://localhost:5173

### 部署时间估算
- 网络正常：约 10-15 分钟
- 模型下载（qwen3:4b）：约 5-8 分钟（取决于网速）

---

## 二、快速启动（已部署过）

如果已经运行过 `deploy.ps1`，后续只需：

```powershell
.\start.ps1
```

---

## 三、手动部署（备选方案）

如果一键脚本失败，可手动按以下步骤操作：

### 1. 安装 Python 3.11+

下载地址：https://www.python.org/downloads/

安装时勾选 **"Add Python to PATH"**

### 2. 创建虚拟环境

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 3. 安装 Node.js 20 LTS

下载地址：https://nodejs.org/

```bash
cd frontend
npm install
```

### 4. 安装 Ollama

下载地址：https://ollama.com/download

```bash
ollama pull qwen3:4b
```

### 5. 下载 CV 模型

```bash
# 手动下载 MediaPipe FaceLandmarker 模型
# 放到 cv_engine/models/face_landmarker.task
```

下载地址：
https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task

### 6. 启动服务

```bash
# 后端（在项目根目录）
.venv\Scripts\python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000

# 前端（在 frontend 目录）
npm run dev
```

---

## 四、常见问题

### 问题1：PowerShell 执行策略限制

**现象**：运行脚本时报错"此系统上禁止运行脚本"

**解决**：
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### 问题2：模型下载失败

**现象**：qwen3:4b 或 face_landmarker.task 下载超时

**解决**：
- 使用国内镜像或手动下载
- qwen3:4b 可换成其他小模型：`ollama pull qwen2.5:3b`

### 问题3：摄像头无法使用

**现象**：浏览器提示"无法访问摄像头"

**解决**：
- 使用 Chrome 浏览器（兼容性最好）
- 确保浏览器摄像头权限已开启
- localhost 不需要 HTTPS，但远程访问需要 HTTPS

### 问题4：Ollama 连接失败

**现象**：后端报错 "Failed to connect to Ollama"

**解决**：
```bash
# 确保 Ollama 服务运行
ollama serve

# 检查服务状态
curl http://localhost:11434/api/tags
```

### 问题5：端口被占用

**现象**：8000 或 5173 端口被占用

**解决**：
```powershell
# 查看端口占用
netstat -ano | findstr :8000

# 结束进程（PID 是上面查到的数字）
taskkill /PID <数字> /F
```

---

## 五、系统要求

| 项目 | 最低要求 | 推荐配置 |
|------|----------|----------|
| 操作系统 | Windows 10 | Windows 11 |
| CPU | 4 核 | 8 核 |
| 内存 | 8 GB | 16 GB |
| GPU | 无（CPU 运行慢） | NVIDIA GPU（Ollama 加速） |
| 磁盘 | 10 GB | 20 GB（含模型） |
| 网络 | 能访问 GitHub | 国内可能需要镜像 |

---

## 六、生产环境部署（可选）

### Docker 部署

```bash
# 构建镜像
docker build -t classvision .

# 运行容器（需要 GPU 支持）
docker run --gpus all -p 8000:8000 -p 5173:5173 classvision
```

**注意**：Docker GPU 支持需要安装 NVIDIA Container Toolkit。

---

## 七、给同学的部署建议

1. **网络检查**：确保能访问 GitHub 和 Google（模型下载）
2. **提前下载**：如果网络慢，可提前手动下载 qwen3:4b 和 face_landmarker.task
3. **重启电脑**：安装完成后建议重启，确保 PATH 生效
4. **Chrome 浏览器**：前端测试用 Chrome，兼容性最好
5. **防火墙**：临时关闭防火墙测试，排除网络问题