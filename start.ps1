# ============================================
# ClassVision 快速启动脚本
# 前提：已完成 deploy.ps1 一键部署
# 使用方式: 右键 -> 使用 PowerShell 运行
# ============================================

$ProjectRoot = $PSScriptRoot
$VenvPython = "$ProjectRoot\.venv\Scripts\python.exe"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "ClassVision 快速启动" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

# 检查虚拟环境
if (-not (Test-Path $VenvPython)) {
    Write-Host "错误: 虚拟环境不存在，请先运行 deploy.ps1" -ForegroundColor Red
    exit 1
}

# 检查 Ollama 服务
Write-Host "检查 Ollama 服务..." -ForegroundColor Yellow
$OllamaRunning = Get-Process -Name "ollama" -ErrorAction SilentlyContinue
if (-not $OllamaRunning) {
    Write-Host "启动 Ollama 服务..." -ForegroundColor Yellow
    Start-Process ollama -ArgumentList "serve" -WindowStyle Hidden
    Start-Sleep -Seconds 3
}

# 启动后端
Write-Host "启动后端服务 (http://localhost:8000)..." -ForegroundColor Yellow
Start-Process -FilePath $VenvPython -ArgumentList "-m", "uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload" -WorkingDirectory $ProjectRoot

# 启动前端
Write-Host "启动前端服务 (http://localhost:5173)..." -ForegroundColor Yellow
Start-Process -FilePath "npm" -ArgumentList "run", "dev" -WorkingDirectory "$ProjectRoot\frontend"

Start-Sleep -Seconds 2

Write-Host "`n========================================" -ForegroundColor Green
Write-Host "服务已启动！" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host "  前端: http://localhost:5173" -ForegroundColor White
Write-Host "  后端: http://localhost:8000" -ForegroundColor White
Write-Host ""

Start-Process "http://localhost:5173"