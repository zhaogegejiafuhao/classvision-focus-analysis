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

# ===== OJ Docker 服务启动 =====
$ojDir = Join-Path $ProjectRoot "oj"
$composeFile = Join-Path $ojDir "docker-compose.yml"
if (Test-Path $composeFile) {
    Write-Host "检查 Docker..." -ForegroundColor Yellow
    $dockerDesktop = Get-Process -Name "Docker Desktop" -ErrorAction SilentlyContinue
    if ($null -eq $dockerDesktop) {
        Write-Host "Docker Desktop 未运行，尝试启动..." -ForegroundColor Yellow
        $dockerExe = "C:\Program Files\Docker\Docker\Docker Desktop.exe"
        if (Test-Path $dockerExe) {
            Start-Process $dockerExe
            Write-Host "等待 Docker 引擎就绪..." -ForegroundColor Yellow
            $dockerReady = $false
            for ($i = 0; $i -lt 60; $i++) {
                try {
                    $null = docker info 2>&1
                    if ($LASTEXITCODE -eq 0) { $dockerReady = $true; break }
                } catch {}
                Start-Sleep -Seconds 2
            }
            if (-not $dockerReady) {
                Write-Host "警告: Docker 引擎未就绪，跳过 OJ 启动" -ForegroundColor Red
            }
        } else {
            Write-Host "警告: 未找到 Docker Desktop，跳过 OJ 启动" -ForegroundColor Red
        }
    }

    # 确认 Docker 可用后启动 OJ 容器
    $dockerOk = $false
    try { $null = docker info 2>&1; if ($LASTEXITCODE -eq 0) { $dockerOk = $true } } catch {}
    if ($dockerOk) {
        Write-Host "启动 OJ Docker 容器..." -ForegroundColor Yellow
        Push-Location $ojDir
        docker-compose up -d 2>&1 | Out-Host
        Pop-Location

        Write-Host "等待 OJ Judger 就绪..." -ForegroundColor Yellow
        $judgerReady = $false
        for ($i = 0; $i -lt 30; $i++) {
            try {
                $resp = Invoke-WebRequest -Uri "http://localhost:12345/ping" -UseBasicParsing -TimeoutSec 2
                if ($resp.Content -eq "pong") { $judgerReady = $true; break }
            } catch {}
            Start-Sleep -Seconds 1
        }
        if ($judgerReady) {
            Write-Host "OJ Judger 已就绪 (port 12345)" -ForegroundColor Green
        } else {
            Write-Host "警告: OJ Judger 30s 内未响应，WebIDE 可能不可用" -ForegroundColor Red
        }
    }
}

Write-Host "启动后端..." -ForegroundColor Yellow
Start-Process -FilePath $VenvPython -ArgumentList "-m","uvicorn","backend.main:app","--host","0.0.0.0","--port","8000","--reload" -WorkingDirectory $ProjectRoot

Write-Host "启动前端..." -ForegroundColor Yellow
$frontendDir = Join-Path $ProjectRoot "frontend"
Start-Process -FilePath "cmd.exe" -ArgumentList "/c","npm run dev" -WorkingDirectory $frontendDir

Start-Sleep -Seconds 4

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "服务已启动！" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host "  前端: http://localhost:5173" -ForegroundColor White
Write-Host "  后端: http://localhost:8000" -ForegroundColor White
Write-Host ""

Start-Process "http://localhost:5173"
