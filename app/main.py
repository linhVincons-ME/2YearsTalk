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
    port = start_port
    while port < start_port + 100:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex((host, port)) != 0:
                return port
            port += 1
    return start_port

def run_server(host: str, port: int):
    """Chạy Uvicorn Server"""
    config = uvicorn.Config(
        app=app,
        host=host,
        port=port,
        log_level="warning",
        access_log=False
    )
    server = uvicorn.Server(config)
    server.run()

def launch_desktop_window(url: str):
    """
    Khởi chạy cửa sổ ứng dụng Desktop Native:
    Ưu tiên 1: Edge / Chrome App Mode (mở riêng biệt như ứng dụng native, hỗ trợ microphone Web Speech API cực mượt)
    Ưu tiên 2: pywebview Native Window
    Ưu tiên 3: Trình duyệt mặc định của hệ thống
    """
    browser_candidates = [
        os.path.expandvars(r"%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe"),
        os.path.expandvars(r"%ProgramFiles%\Microsoft\Edge\Application\msedge.exe"),
        os.path.expandvars(r"%ProgramFiles%\Google\Chrome\Application\chrome.exe"),
        os.path.expandvars(r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"),
        os.path.expandvars(r"%LocalAppData%\Google\Chrome\Application\chrome.exe"),
        os.path.expandvars(r"%LocalAppData%\Microsoft\Edge\Application\msedge.exe"),
    ]

    for browser_path in browser_candidates:
        if os.path.exists(browser_path):
            try:
                print(f"🖥️  Khởi chạy cửa sổ Desktop chuyên dụng qua: {os.path.basename(browser_path)}")
                cmd = [
                    browser_path,
                    f"--app={url}",
                    "--window-size=1300,850",
                    "--window-position=50,50",
                    "--disable-features=Translate",
                    "--enable-features=WebSpeechAPI",
                    "--autoplay-policy=no-user-gesture-required"
                ]
                proc = subprocess.Popen(cmd)
                proc.wait()
                print("👋 Ứng dụng Bé Tập Nói đã được đóng.")
                return True
            except Exception as e:
                print(f"[*] Thử phương thức tiếp theo: {e}")

    # Thử qua pywebview
    try:
        import webview
        print("🖥️  Khởi chạy qua pywebview...")
        window = webview.create_window(
            title=APP_TITLE,
            url=url,
            width=1300,
            height=850,
            min_size=(960, 640),
            text_select=True
        )
        webview.start(debug=False)
        print("👋 Ứng dụng Bé Tập Nói đã được đóng.")
        return True
    except Exception:
        pass

    # Fallback mở browser
    print("🌐 Mở ứng dụng trên trình duyệt mặc định...")
    webbrowser.open(url)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    return False

def main():
    parser = argparse.ArgumentParser(description="Khởi chạy ứng dụng Bé Tập Nói Desktop")
    parser.add_argument("--host", default=DEFAULT_HOST, help="Host để bind web server")
    parser.add_argument("--port", type=int, default=None, help="Cổng chạy web server")
    parser.add_argument("--web", action="store_true", help="Chạy ở chế độ trình duyệt Web thông thường")
    args = parser.parse_args()

    actual_port = args.port if args.port else find_available_port(args.host, DEFAULT_PORT)
    url = f"http://{args.host}:{actual_port}"

    print("=" * 65)
    print(f"🌸 {APP_TITLE}")
    print(f"✨ Phiên bản: {APP_VERSION}")
    print(f"🌐 Địa chỉ Backend: {url}")
    print("=" * 65)

    if args.web:
        webbrowser.open(url)
        uvicorn.run("app.main:app", host=args.host, port=actual_port, reload=False)
        return

    # Khởi động server trong background thread
    server_thread = threading.Thread(target=run_server, args=(args.host, actual_port), daemon=True)
    server_thread.start()

    # Đợi server sẵn sàng
    max_wait = 10.0
    start_time = time.time()
    server_ready = False
    while time.time() - start_time < max_wait:
        try:
            with urllib.request.urlopen(f"{url}/api/stats", timeout=1) as resp:
                if resp.status == 200:
                    server_ready = True
                    break
        except Exception:
            time.sleep(0.3)

    if not server_ready:
        print("⚠️ Không thể kết nối tới server, mở trình duyệt mặc định...")
        webbrowser.open(url)
        return

    # Mở cửa sổ Desktop
    launch_desktop_window(url)

if __name__ == "__main__":
    main()
