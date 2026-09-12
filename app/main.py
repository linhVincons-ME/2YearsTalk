"""
Khởi chạy Backend và Cửa Sổ Desktop Ứng Dụng Bé Tập Nói (BeTapNoi)
"""
import sys
import os
import time
import socket
import urllib.request
import webbrowser
import threading
import argparse
import subprocess
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.config import DEFAULT_HOST, DEFAULT_PORT, STATIC_DIR, APP_TITLE, APP_VERSION
from app.database import init_db
from app.routes.api import router as api_router

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

# Khởi tạo ứng dụng FastAPI
app = FastAPI(
    title=APP_TITLE,
    version=APP_VERSION,
    description="Ứng dụng Đào tạo & Huấn luyện Bé Tập Nói Tiếng Việt 2-5 Tuổi",
    lifespan=lifespan
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Đăng ký routes
app.include_router(api_router)

# Mount thư mục static
if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

@app.get("/")
def get_index():
    """Phục vụ file index.html chính"""
    index_file = STATIC_DIR / "index.html"
    if index_file.exists():
        return FileResponse(str(index_file))
    return {"message": "Bé Tập Nói Server đang hoạt động. Vui lòng tải index.html."}

def find_available_port(host: str = DEFAULT_HOST, start_port: int = DEFAULT_PORT) -> int:
    """Tự động tìm cổng còn trống nếu cổng mặc định đã bị chiếm"""
    for port in range(start_port, start_port + 50):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind((host, port))
                return port
            except OSError:
                continue
    return start_port

def open_desktop_window_delayed(url: str, delay: float = 1.0):
    """Mở cửa sổ Desktop ứng dụng trong luồng nền sau khi server đã sẵn sàng"""
    def _launcher():
        time.sleep(delay)
        opened = False
        browser_candidates = [
            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Edge\Application\msedge.exe"),
            os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
        ]

        for browser_path in browser_candidates:
            if os.path.isfile(browser_path):
                try:
                    print(f"🖥️  Đang mở cửa sổ giao diện ứng dụng ({os.path.basename(browser_path)})...")
                    cmd = [
                        browser_path,
                        f"--app={url}",
                        "--new-window",
                        "--window-size=1340,880",
                        "--app-auto-launched"
                    ]
                    subprocess.Popen(cmd)
                    opened = True
                    break
                except Exception as e:
                    print(f"[*] Lỗi mở qua {os.path.basename(browser_path)}: {e}")

        if not opened:
            print("🌐 Đang mở ứng dụng trên trình duyệt mặc định...")
            webbrowser.open(url)

    thread = threading.Thread(target=_launcher, daemon=True)
    thread.start()

def main():
    parser = argparse.ArgumentParser(description="Khởi chạy ứng dụng Bé Tập Nói Desktop")
    parser.add_argument("--host", default=DEFAULT_HOST, help="Host để bind web server")
    parser.add_argument("--port", type=int, default=None, help="Cổng chạy web server")
    parser.add_argument("--no-open", action="store_true", help="Không tự động mở giao diện")
    args = parser.parse_args()

    actual_port = args.port if args.port else find_available_port(args.host, DEFAULT_PORT)
    url = f"http://{args.host}:{actual_port}"

    print("=" * 65)
    print(f"🌸 {APP_TITLE}")
    print(f"✨ Phiên bản: {APP_VERSION}")
    print(f"🌐 Ứng dụng hoạt động tại: {url}")
    print("=" * 65)

    if not args.no_open:
        open_desktop_window_delayed(url, delay=1.0)

    # Chạy uvicorn trực tiếp trên main thread
    uvicorn.run("app.main:app", host=args.host, port=actual_port, log_level="warning", reload=False)

if __name__ == "__main__":
    main()
