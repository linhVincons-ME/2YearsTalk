@echo off
setlocal
cd /d "%~dp0"
title Be Tap Noi - Tieng Viet Cho Be (2-5 Tuoi)

echo ====================================================
echo      Be Tap Noi - Vietnamese Speech Suite
echo ====================================================

REM Kiem tra moi truong ao .venv
if not exist ".venv\Scripts\python.exe" (
    echo [1/2] Khoi tao moi truong ao Python .venv...
    if exist "D:\Pinokio\bin\miniconda\python.exe" (
        "D:\Pinokio\bin\miniconda\python.exe" -m venv .venv
    ) else if exist "D:\Pinokio\bin\miniforge\python.exe" (
        "D:\Pinokio\bin\miniforge\python.exe" -m venv .venv
    ) else (
        python -m venv .venv
    )
    echo [2/2] Cai dat thu vien lan dau...
    ".venv\Scripts\python.exe" -m pip install -r requirements.txt
)

REM Khoi chay Desktop Application ngay lap tuc
echo [*] Dang khoi dong ung dung Be Tap Noi...
".venv\Scripts\python.exe" main.py %*

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [!] Chuong trinh gap loi khi khoi chay.
    pause
)
