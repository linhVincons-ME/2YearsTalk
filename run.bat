@echo off
setlocal
cd /d "%~dp0"
title Be Tap Noi - Tieng Viet Cho Be (2-5 Tuoi)

echo ====================================================
echo      Be Tap Noi - Vietnamese Speech Suite
echo ====================================================

REM 1. Kiem tra moi truong ao .venv
if not exist ".venv\Scripts\python.exe" (
    echo [1/3] Khoi tao moi truong ao Python .venv...
    if exist "D:\Pinokio\bin\miniconda\python.exe" (
        "D:\Pinokio\bin\miniconda\python.exe" -m venv .venv
    ) else if exist "D:\Pinokio\bin\miniforge\python.exe" (
        "D:\Pinokio\bin\miniforge\python.exe" -m venv .venv
    ) else (
        python -m venv .venv
    )
)

REM 2. Kiem tra va cai dat thu vien
echo [2/3] Kiem tra va cai dat thu vien requirements.txt...
".venv\Scripts\python.exe" -m pip install -r requirements.txt --quiet

REM 3. Khoi chay Desktop Application
echo [3/3] Khoi chay ung dung Be Tap Noi...
".venv\Scripts\python.exe" main.py %*

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [!] Chuong trinh gap loi khi khoi chay.
    pause
)
