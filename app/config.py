"""
Cấu hình ứng dụng Bé Tập Nói (BeTapNoi)
"""
import os
from pathlib import Path

# Thư mục gốc dự án
BASE_DIR = Path(__file__).resolve().parent.parent

# Thư mục tĩnh và cơ sở dữ liệu
STATIC_DIR = BASE_DIR / "app" / "static"
DATA_DIR = BASE_DIR / "app" / "data"
DATABASE_PATH = BASE_DIR / "betapnoi.db"

# Cấu hình Web Server
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8088

# Thông tin ứng dụng
APP_TITLE = "Bé Tập Nói - Ứng Dụng Học Nói Tiếng Việt Cho Bé 2-5 Tuổi"
APP_VERSION = "1.0.0"
