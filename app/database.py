"""
Quản lý cơ sở dữ liệu SQLite cho ứng dụng Bé Tập Nói
"""
import sqlite3
import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional
from app.config import DATABASE_PATH

def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Khởi tạo cấu trúc các bảng dữ liệu nếu chưa tồn tại"""
    conn = get_connection()
    cursor = conn.cursor()

    # Bảng thông tin tổng quan của bé
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_profile (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT DEFAULT 'Bé Yêu',
        avatar TEXT DEFAULT '👶',
        age_selected TEXT DEFAULT 'age_2',
        total_stars INTEGER DEFAULT 0,
        words_learned INTEGER DEFAULT 0,
        total_seconds INTEGER DEFAULT 0,
        streak_days INTEGER DEFAULT 1,
        last_active_date TEXT,
        created_at TEXT
    )
    """)

    # Bảng ghi nhận từ / bài học bé đã học
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS learned_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_id TEXT UNIQUE,
        age_group TEXT,
        category TEXT,
        stars INTEGER DEFAULT 1,
        practice_count INTEGER DEFAULT 1,
        last_practiced_at TEXT
    )
    """)

    # Bảng lịch sử phát âm / luyện nói
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS speech_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        target_text TEXT,
        spoken_text TEXT,
        score INTEGER,
        stars INTEGER,
        age_group TEXT,
        created_at TEXT
    )
    """)

    # Bảng huy hiệu thành tích của bé
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS badges (
        id TEXT PRIMARY KEY,
        name TEXT,
        description TEXT,
        icon TEXT,
        unlocked INTEGER DEFAULT 0,
        unlocked_at TEXT
    )
    """)

    # Bảng cài đặt hệ thống
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS app_settings (
        key TEXT PRIMARY KEY,
        value TEXT
    )
    """)

    # Tạo hồ sơ mặc định nếu chưa có
    cursor.execute("SELECT COUNT(*) as count FROM user_profile")
    if cursor.fetchone()["count"] == 0:
        today_str = datetime.date.today().isoformat()
        cursor.execute("""
            INSERT INTO user_profile (name, avatar, age_selected, total_stars, words_learned, total_seconds, streak_days, last_active_date, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, ('Bé Yêu', '👶', 'age_2', 15, 5, 300, 1, today_str, today_str))

    # Nạp danh sách huy hiệu chuẩn nếu chưa có
    default_badges = [
        ("first_word", "Bật Âm Đầu Đời", "Bé đã phát âm thành công từ đầu tiên!", "🌱", 1),
        ("star_collector_10", "Thợ Săn 10 Ngôi Sao", "Bé đã tích lũy được 10 ngôi sao lấp lánh!", "⭐", 1),
        ("rhyme_master", "Bạn Nhỏ Thuộc Đồng Dao", "Bé đọc vang bài đồng dao vui nhộn!", "🎵", 0),
        ("story_teller", "Nhà Kể Chuyện Nhí", "Bé đã kể xong một câu chuyện tranh sinh động!", "📖", 0),
        ("alphabet_explorer", "Thám Hiểm Chữ Cái", "Bé nhận biết và đọc đúng các chữ cái tiếng Việt!", "🅰️", 0),
        ("speech_champion", "Quán Quân Giọng Nói Rõ Ràng", "Bé nói to, rõ ràng và đạt điểm tối đa!", "🏆", 0),
    ]
    for b_id, name, desc, icon, unlocked in default_badges:
        cursor.execute("SELECT COUNT(*) as count FROM badges WHERE id = ?", (b_id,))
        if cursor.fetchone()["count"] == 0:
            unlocked_time = datetime.datetime.now().isoformat() if unlocked else None
            cursor.execute("""
                INSERT INTO badges (id, name, description, icon, unlocked, unlocked_at)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (b_id, name, desc, icon, unlocked, unlocked_time))

    # Cài đặt mặc định
    default_settings = {
        "voice_accent": "north",
        "eye_care_minutes": "20",
        "sound_effects": "true",
        "bg_music": "true"
    }
    for k, v in default_settings.items():
        cursor.execute("INSERT OR IGNORE INTO app_settings (key, value) VALUES (?, ?)", (k, v))

    conn.commit()
    conn.close()

def get_profile() -> Dict[str, Any]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_profile LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    if row:
        return dict(row)
    return {
        "name": "Bé Yêu",
        "avatar": "👶",
        "age_selected": "age_2",
        "total_stars": 0,
        "words_learned": 0,
        "total_seconds": 0,
        "streak_days": 1
    }

def record_practice(item_id: str, age_group: str, category: str, stars: int, duration_seconds: int = 30) -> Dict[str, Any]:
    conn = get_connection()
    cursor = conn.cursor()
    now_str = datetime.datetime.now().isoformat()

    # Kiểm tra xem từ này đã học chưa
    cursor.execute("SELECT * FROM learned_items WHERE item_id = ?", (item_id,))
    row = cursor.fetchone()
    is_new = False
    if row:
        cursor.execute("""
            UPDATE learned_items 
            SET practice_count = practice_count + 1,
                stars = MAX(stars, ?),
                last_practiced_at = ?
            WHERE item_id = ?
        """, (stars, now_str, item_id))
    else:
        is_new = True
        cursor.execute("""
            INSERT INTO learned_items (item_id, age_group, category, stars, practice_count, last_practiced_at)
            VALUES (?, ?, ?, ?, 1, ?)
        """, (item_id, age_group, category, stars, now_str))

    # Cập nhật hồ sơ bé
    words_add = 1 if is_new else 0
    cursor.execute("""
        UPDATE user_profile
        SET total_stars = total_stars + ?,
            words_learned = words_learned + ?,
            total_seconds = total_seconds + ?
    """, (stars, words_add, duration_seconds))

    # Kiểm tra mở khóa huy hiệu
    cursor.execute("SELECT total_stars, words_learned FROM user_profile LIMIT 1")
    prof = cursor.fetchone()
    if prof:
        if prof["total_stars"] >= 10:
            cursor.execute("UPDATE badges SET unlocked = 1, unlocked_at = ? WHERE id = 'star_collector_10' AND unlocked = 0", (now_str,))
        if prof["words_learned"] >= 1:
            cursor.execute("UPDATE badges SET unlocked = 1, unlocked_at = ? WHERE id = 'first_word' AND unlocked = 0", (now_str,))

    conn.commit()

    cursor.execute("SELECT total_stars, words_learned, total_seconds FROM user_profile LIMIT 1")
    updated = cursor.fetchone()
    conn.close()
    return dict(updated) if updated else {}

def save_speech_record(target: str, spoken: str, score: int, stars: int, age_group: str):
    conn = get_connection()
    cursor = conn.cursor()
    now_str = datetime.datetime.now().isoformat()
    cursor.execute("""
        INSERT INTO speech_records (target_text, spoken_text, score, stars, age_group, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (target, spoken, score, stars, age_group, now_str))

    if score >= 90:
        cursor.execute("UPDATE badges SET unlocked = 1, unlocked_at = ? WHERE id = 'speech_champion' AND unlocked = 0", (now_str,))

    cursor.execute("UPDATE user_profile SET total_stars = total_stars + ?", (stars,))
    conn.commit()
    conn.close()

def get_badges_list() -> List[Dict[str, Any]]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM badges ORDER BY unlocked DESC, id ASC")
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_settings() -> Dict[str, str]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT key, value FROM app_settings")
    rows = cursor.fetchall()
    conn.close()
    return {r["key"]: r["value"] for r in rows}

def update_setting(key: str, value: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO app_settings (key, value) VALUES (?, ?)", (key, value))
    conn.commit()
    conn.close()
