# Bé Tập Nói - Kịch bản khởi chạy PowerShell
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "===================================================================" -ForegroundColor Cyan
Write-Host "🌸 Khởi động Ứng Dụng Bé Tập Nói (BeTapNoi - Vietnamese for Kids)" -ForegroundColor Magenta
Write-Host "===================================================================" -ForegroundColor Cyan

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

$venvPython = Join-Path $scriptDir ".venv\Scripts\python.exe"

if (-not (Test-Path $venvPython)) {
    Write-Host "[*] Tạo môi trường ảo .venv..." -ForegroundColor Yellow
    & "D:\Pinokio\bin\miniconda\python.exe" -m venv .venv
    & .\.venv\Scripts\pip.exe install -r requirements.txt
}

Write-Host "[*] Khởi chạy cửa sổ Desktop Bé Tập Nói..." -ForegroundColor Green
& $venvPython main.py
