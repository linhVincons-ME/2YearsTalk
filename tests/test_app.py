"""
Kiểm thử tự động cho ứng dụng Bé Tập Nói (BeTapNoi)
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import init_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_database():
    """Khởi tạo database trước mỗi bài test"""
    init_db()

def test_get_index():
    """Kiểm tra trang chủ index.html được tải chính xác"""
    response = client.get("/")
    assert response.status_code == 200
    assert "Bé Tập Nói" in response.text
    assert "age-tabs" in response.text

def test_get_curriculum_overview():
    """Kiểm tra danh mục tổng hợp 4 độ tuổi mầm non"""
    response = client.get("/api/curriculum")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert len(data["curriculums"]) == 4

    keys = [c["key"] for c in data["curriculums"]]
    assert "age_2" in keys
    assert "age_3" in keys
    assert "age_4" in keys
    assert "age_5" in keys

def test_get_curriculum_age_2():
    """Kiểm tra giáo trình lớp 2 tuổi (Bật âm, từ đơn/đôi)"""
    response = client.get("/api/curriculum/age_2")
    assert response.status_code == 200
    data = response.json()["data"]
    assert "categories" in data
    cat_ids = [c["id"] for c in data["categories"]]
    assert "animal_sounds" in cat_ids
    assert "family" in cat_ids
    assert "daily_needs" in cat_ids

def test_get_curriculum_age_3():
    """Kiểm tra giáo trình lớp 3 tuổi (Màu sắc, hình khối, ghép câu)"""
    response = client.get("/api/curriculum/age_3")
    assert response.status_code == 200
    data = response.json()["data"]
    cat_ids = [c["id"] for c in data["categories"]]
    assert "colors_shapes" in cat_ids
    assert "sentence_building" in cat_ids

def test_get_curriculum_age_4():
    """Kiểm tra giáo trình lớp 4 tuổi (Đồng dao và kể chuyện tranh)"""
    response = client.get("/api/curriculum/age_4")
    assert response.status_code == 200
    data = response.json()["data"]
    assert "rhymes" in data
    assert len(data["rhymes"]) >= 3
    assert "stories" in data
    assert len(data["stories"]) >= 2

def test_get_curriculum_age_5():
    """Kiểm tra giáo trình lớp 5 tuổi (29 chữ cái, 6 thanh điệu, ghép vần)"""
    response = client.get("/api/curriculum/age_5")
    assert response.status_code == 200
    data = response.json()["data"]
    assert "tones" in data
    assert len(data["tones"]) == 6
    assert "alphabet" in data
    assert len(data["alphabet"]) == 29
    assert "blending_lessons" in data

def test_parenting_guide():
    """Kiểm tra cẩm nang âm ngữ trị liệu cho phụ huynh"""
    response = client.get("/api/parenting-guide")
    assert response.status_code == 200
    data = response.json()
    assert "guides" in data
    assert len(data["guides"]) >= 4

def test_stats_and_practice_record():
    """Kiểm tra ghi nhận tiến độ và cộng điểm thưởng sao"""
    # Lấy thông tin ban đầu
    res_before = client.get("/api/stats")
    assert res_before.status_code == 200
    stars_before = res_before.json()["total_stars"]

    # Ghi nhận bé học xong 1 từ
    record_payload = {
        "age_group": "age_2",
        "item_id": "test_dog_item",
        "category": "animal_sounds",
        "stars_earned": 3,
        "duration_seconds": 30
    }
    res_record = client.post("/api/practice/record", json=record_payload)
    assert res_record.status_code == 200

    # Kiểm tra số sao sau khi ghi nhận
    res_after = client.get("/api/stats")
    stars_after = res_after.json()["total_stars"]
    assert stars_after >= stars_before + 3

def test_speech_evaluation_age_2_encouragement():
    """Kiểm tra đánh giá phát âm cho bé 2 tuổi: luôn khích lệ nỗ lực bật âm"""
    payload = {
        "target_text": "Ba ơi",
        "spoken_text": "ba",
        "age_group": "age_2"
    }
    response = client.post("/api/speech/evaluate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["stars"] >= 2
    assert data["score"] >= 75
    assert "Hoan hô" in data["feedback"] or "Bé" in data["feedback"]

def test_speech_evaluation_exact_match():
    """Kiểm tra phát âm chuẩn xác cho trẻ lớn"""
    payload = {
        "target_text": "Con muốn ăn táo",
        "spoken_text": "Con muốn ăn táo",
        "age_group": "age_3"
    }
    response = client.post("/api/speech/evaluate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["is_match"] is True
    assert data["stars"] == 3
    assert data["score"] >= 90
