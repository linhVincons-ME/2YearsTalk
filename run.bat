@echo off
chcp 65001 > nul
title Bé Tập Nói - Ứng Dụng Học Nói Tiếng Việt (2-5 Tuổi)

echo ===================================================================
echo 🌸 Khởi động Ứng Dụng Bé Tập Nói (BeTapNoi - Vietnamese for Kids)
echo ===================================================================

cd /d "%~dp0"

REM Kiểm tra môi trường ảo
if not exist ".venv\Scripts\python.exe" (
    echo [*] Đang thiết lập môi trường ảo Python...
    "D:\Pinokio\bin\miniconda\python.exe" -m venv .venv
    call .venv\Scripts\pip.exe install -r requirements.txt
)

echo [*] Khởi chạy cửa sổ ứng dụng Bé Tập Nói Desktop...
call .venv\Scripts\python.exe main.py

if %errorlevel% neq 0 (
    echo.
    echo [!] Đã xảy ra sự cố khi khởi chạy. Vui lòng kiểm tra lại môi trường Python.
    pause
)
