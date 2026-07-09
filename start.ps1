# ClassVision 快速启动脚本
# 使用方式: 右键 -> 使用 PowerShell 运行

$ProjectRoot = $PSScriptRoot
$VenvPython = Join-Path $ProjectRoot ".venv\Scripts\python.exe"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "ClassVision 快速启动" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

$policy = Get-ExecutionPolicy -Scope CurrentUser
if (($policy -eq "Restricted") -or ($policy -eq "Undefined")) {
    Write-Host "正在设置执行策略..." -ForegroundColor Yellow
    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force
}

if (-not (Test-Path $VenvPython)) {
    Write-Host "错误: 虚拟环境不存在，请先运行 deploy.ps1" -ForegroundColor Red
    Read-Host "按回车退出"
    exit 1
}

Write-Host "检查 Ollama 服务..." -ForegroundColor Yellow
$ollama = Get-Process -Name "ollama" -ErrorAction SilentlyContinue
if ($null -eq $ollama) {
    Write-Host "启动 Ollama..." -ForegroundColor Yellow
    Start-Process ollama -ArgumentList "serve" -WindowStyle Hidden
    Start-Sleep -Seconds 3
}

Write-Host "启动后端..." -ForegroundColor Yellow
Start-Process -FilePath $VenvPython -ArgumentList "-m","uvicorn","backend.main:app","--host","0.0.0.0","--port","8000","--reload" -WorkingDirectory $ProjectRoot

Write-Host "启动前端..." -ForegroundColor Yellow
$frontendDir = Join-Path $ProjectRoot "frontend"
Start-Process -FilePath "cmd.exe" -ArgumentList "/c","npm run dev" -WorkingDirectory $frontendDir

Start-Sleep -Seconds 2

Write-Host "等待后端就绪..." -ForegroundColor Yellow
$backendReady = $false
for ($i = 0; $i -lt 30; $i++) {
    try {
        $response = Invoke-RestMethod -Uri "http://localhost:8000/api/health" -Method Get -TimeoutSec 2 -ErrorAction Stop
        if ($response.status -eq "ok") {
            $backendReady = $true
            break
        }
    } catch {
        Start-Sleep -Seconds 2
    }
}

if ($backendReady) {
    Write-Host "后端已就绪！" -ForegroundColor Green
} else {
    Write-Host "警告: 后端未在60秒内就绪，前端可能无法加载数据" -ForegroundColor Red
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "服务已启动！" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host "  前端: http://localhost:5173" -ForegroundColor White
Write-Host "  后端: http://localhost:8000" -ForegroundColor White
Write-Host ""

Start-Process "http://localhost:5173"
