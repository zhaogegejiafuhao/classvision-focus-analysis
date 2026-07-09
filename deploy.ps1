# ============================================
# ClassVision 一键部署脚本 (Windows PowerShell)
# 使用方式: 右键 -> 使用 PowerShell 运行
# 或在 PowerShell 中执行: .\deploy.ps1
# ============================================

param(
    [switch]$SkipOllama,    # 跳过 Ollama 安装（如果已安装）
    [switch]$SkipModels,    # 跳过模型下载（如果已下载）
    [switch]$StartOnly      # 仅启动服务（假设已部署）
)

$ErrorActionPreference = "Stop"
$ProjectRoot = $PSScriptRoot

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "ClassVision 一键部署脚本" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

# ============================================
# 第一步：检查 Python 环境
# ============================================
Write-Host "`n[1/6] 检查 Python 环境..." -ForegroundColor Yellow

$PythonCmd = $null
$PythonPaths = @(
    "$ProjectRoot\.venv\Scripts\python.exe",
    "python.exe",
    "python3.exe",
    "py.exe"
)

foreach ($path in $PythonPaths) {
    try {
        $version = & $path --version 2>$null
        if ($version -match 'Python 3\.(1[1-9]|[2-9]\d)') {
            $PythonCmd = $path
            Write-Host "找到 Python: $path ($version)" -ForegroundColor Green
            break
        }
    } catch {}
}

if (-not $PythonCmd) {
    Write-Host "未找到 Python 3.10+，正在尝试安装..." -ForegroundColor Red

    # 下载 Python 3.11
    $PythonInstaller = "$env:TEMP\python-installer.exe"
    $PythonUrl = "https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe"

    Write-Host "下载 Python 3.11..." -ForegroundColor Yellow
    Invoke-WebRequest -Uri $PythonUrl -OutFile $PythonInstaller -UseBasicParsing

    Write-Host "安装 Python（静默模式，添加到 PATH）..." -ForegroundColor Yellow
    Start-Process -FilePath $PythonInstaller -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1 Include_test=0" -Wait

    # 刷新 PATH
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")

    $PythonCmd = "python.exe"
    Write-Host "Python 安装完成" -ForegroundColor Green
}

# ============================================
# 第二步：创建虚拟环境并安装依赖
# ============================================
Write-Host "`n[2/6] 安装 Python 依赖..." -ForegroundColor Yellow

if (-not (Test-Path "$ProjectRoot\.venv")) {
    Write-Host "创建虚拟环境..." -ForegroundColor Yellow
    & $PythonCmd -m venv "$ProjectRoot\.venv"
}

$VenvPython = "$ProjectRoot\.venv\Scripts\python.exe"
$VenvPip = "$ProjectRoot\.venv\Scripts\pip.exe"

Write-Host "升级 pip..." -ForegroundColor Yellow
& $VenvPython -m pip install --upgrade pip --quiet

Write-Host "安装项目依赖 (requirements.txt)..." -ForegroundColor Yellow
& $VenvPip install -r "$ProjectRoot\requirements.txt" --quiet

Write-Host "Python 依赖安装完成" -ForegroundColor Green

# ============================================
# 第三步：检查 Node.js 环境
# ============================================
Write-Host "`n[3/6] 检查 Node.js 环境..." -ForegroundColor Yellow

try {
    $NodeVersion = & node --version 2>$null
    if ($NodeVersion -match 'v(1[8-9]|[2-9]\d)') {
        Write-Host "Node.js 已安装: $NodeVersion" -ForegroundColor Green
    } else {
        throw "Node.js 版本过低"
    }
} catch {
    Write-Host "未找到 Node.js 18+，正在尝试安装..." -ForegroundColor Red

    # 使用 winget 安装（Windows 10/11 内置）
    if (Get-Command winget -ErrorAction SilentlyContinue) {
        Write-Host "使用 winget 安装 Node.js..." -ForegroundColor Yellow
        winget install OpenJS.NodeJS.LTS --accept-source-agreements --accept-package-agreements
    } else {
        # 手动下载
        $NodeInstaller = "$env:TEMP\node-installer.msi"
        $NodeUrl = "https://nodejs.org/dist/v20.18.0/node-v20.18.0-x64.msi"

        Write-Host "下载 Node.js 20 LTS..." -ForegroundColor Yellow
        Invoke-WebRequest -Uri $NodeUrl -OutFile $NodeInstaller -UseBasicParsing

        Write-Host "安装 Node.js..." -ForegroundColor Yellow
        Start-Process msiexec.exe -ArgumentList "/i $NodeInstaller /qn" -Wait
    }

    # 刷新 PATH
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")
    Write-Host "Node.js 安装完成" -ForegroundColor Green
}

# ============================================
# 第四步：安装前端依赖
# ============================================
Write-Host "`n[4/6] 安装前端依赖..." -ForegroundColor Yellow

Push-Location "$ProjectRoot\frontend"
try {
    & npm install --loglevel=error
    Write-Host "前端依赖安装完成" -ForegroundColor Green
} finally {
    Pop-Location
}

# ============================================
# 第五步：检查 Ollama 和模型
# ============================================
if (-not $SkipOllama) {
    Write-Host "`n[5/6] 检查 Ollama..." -ForegroundColor Yellow

    try {
        $OllamaVersion = & ollama --version 2>$null
        Write-Host "Ollama 已安装: $OllamaVersion" -ForegroundColor Green
    } catch {
        Write-Host "Ollama 未安装，正在下载..." -ForegroundColor Red

        $OllamaInstaller = "$env:TEMP\ollama-setup.exe"
        $OllamaUrl = "https://github.com/ollama/ollama/releases/download/v0.5.7/OllamaSetup.exe"

        Write-Host "下载 Ollama 安装程序..." -ForegroundColor Yellow
        Invoke-WebRequest -Uri $OllamaUrl -OutFile $OllamaInstaller -UseBasicParsing

        Write-Host "安装 Ollama..." -ForegroundColor Yellow
        Start-Process -FilePath $OllamaInstaller -Wait

        # 刷新 PATH
        $env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")
        Write-Host "Ollama 安装完成" -ForegroundColor Green

        # 启动 Ollama 服务
        Write-Host "启动 Ollama 服务..." -ForegroundColor Yellow
        Start-Process ollama -ArgumentList "serve" -WindowStyle Hidden
        Start-Sleep -Seconds 5
    }
}

if (-not $SkipModels) {
    Write-Host "`n下载 AI 模型 (qwen3:4b)..." -ForegroundColor Yellow

    # 检查模型是否已存在
    $Models = & ollama list 2>$null
    if ($Models -notmatch "qwen3:4b") {
        Write-Host "正在下载 qwen3:4b 模型（约 2.5GB，请耐心等待）..." -ForegroundColor Yellow
        & ollama pull qwen3:4b
        Write-Host "模型下载完成" -ForegroundColor Green
    } else {
        Write-Host "qwen3:4b 模型已存在" -ForegroundColor Green
    }

    # 检查 CV 模型文件
    Write-Host "`n检查 CV 模型文件..." -ForegroundColor Yellow

    $ModelDir = "$ProjectRoot\cv_engine\models"
    $FaceLandmarker = "$ModelDir\face_landmarker.task"

    if (-not (Test-Path $FaceLandmarker)) {
        Write-Host "下载 MediaPipe FaceLandmarker 模型..." -ForegroundColor Yellow
        $ModelUrl = "https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task"
        Invoke-WebRequest -Uri $ModelUrl -OutFile $FaceLandmarker -UseBasicParsing
        Write-Host "FaceLandmarker 模型下载完成" -ForegroundColor Green
    } else {
        Write-Host "FaceLandmarker 模型已存在" -ForegroundColor Green
    }
}

# ============================================
# 第六步：启动服务
# ============================================
Write-Host "`n[6/6] 启动服务..." -ForegroundColor Yellow

Write-Host "`n部署完成！正在启动服务..." -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

# 启动后端
Write-Host "启动后端服务 (http://localhost:8000)..." -ForegroundColor Yellow
Start-Process -FilePath $VenvPython -ArgumentList "-m", "uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000" -WorkingDirectory $ProjectRoot

# 启动前端
Write-Host "启动前端服务 (http://localhost:5173)..." -ForegroundColor Yellow
Start-Process -FilePath "cmd.exe" -ArgumentList "/c", "npm run dev" -WorkingDirectory "$ProjectRoot\frontend"

Start-Sleep -Seconds 3

Write-Host "`n========================================" -ForegroundColor Green
Write-Host "ClassVision 已成功启动！" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "访问地址：" -ForegroundColor Cyan
Write-Host "  前端界面: http://localhost:5173" -ForegroundColor White
Write-Host "  后端 API: http://localhost:8000/api/health" -ForegroundColor White
Write-Host ""
Write-Host "注意事项：" -ForegroundColor Yellow
Write-Host "  - 请确保摄像头可用（Chrome 浏览器最佳）" -ForegroundColor White
Write-Host "  - Ollama 服务会在后台持续运行" -ForegroundColor White
Write-Host "  - 按 Ctrl+C 可停止脚本，但服务会继续运行" -ForegroundColor White
Write-Host ""

# 打开浏览器
Start-Process "http://localhost:5173"