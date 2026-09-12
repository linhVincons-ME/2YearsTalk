"""
FastAPI Routes cho Bé Tập Nói (BeTapNoi)
"""
import re
import difflib
from typing import Optional, Dict, Any
from fastapi import APIRouter, HTTPException, Query

from app.data.curriculum_data import CURRICULUM_DATA, PARENTING_GUIDE
from app.database import (
    get_profile,
    record_practice,
    save_speech_record,
    get_badges_list,
    get_settings,
    update_setting
)
from app.models.schemas import (
    SpeechEvaluateRequest,
    SpeechEvaluateResponse,
    PracticeProgressRequest,
    UserStats,
    SettingsUpdate
)

router = APIRouter(prefix="/api", tags=["Bé Tập Nói API"])

def normalize_text(text: str) -> str:
    """Chuẩn hóa văn bản tiếng Việt để so sánh"""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text

@router.get("/curriculum")
def get_all_curriculums():
    """Lấy danh sách các lộ trình đào tạo theo 4 độ tuổi"""
    overview = []
    for key, val in CURRICULUM_DATA.items():
        overview.append({
            "key": key,
            "title": val["title"],
            "stage": val["stage"],
            "description": val["description"],
            "milestones": val["milestones"]
        })
    return {"status": "success", "curriculums": overview}

@router.get("/curriculum/{age_group}")
def get_curriculum_by_age(age_group: str):
    """Lấy chi tiết bài học và tài liệu của một độ tuổi cụ thể (age_2, age_3, age_4, age_5)"""
    if age_group not in CURRICULUM_DATA:
        raise HTTPException(status_code=404, detail=f"Không tìm thấy lộ trình cho nhóm tuổi: {age_group}")
    return {"status": "success", "data": CURRICULUM_DATA[age_group]}

@router.get("/parenting-guide")
def get_parenting_tips():
    """Lấy cẩm nang hướng dẫn phụ huynh & chuyên gia âm ngữ trị liệu"""
    return {"status": "success", "guides": PARENTING_GUIDE}

@router.get("/stats", response_model=UserStats)
def get_stats():
    """Lấy thống kê học tập và tiến độ của bé"""
    profile = get_profile()
    badges = get_badges_list()
    
    total_seconds = profile.get("total_seconds", 0)
    minutes = max(1, total_seconds // 60)

    # Đánh giá danh hiệu theo số sao
    stars = profile.get("total_stars", 0)
    if stars < 20:
        level = "Mầm Non Tập Bật Âm 🌱"
    elif stars < 50:
        level = "Bé Yêu Nói Chuẩn 🌟"
    elif stars < 100:
        level = "Ngôi Sao Hoạt Ngôn 🏆"
    else:
        level = "Bậc Thầy Ngôn Ngữ Nhí 👑"

    return UserStats(
        total_stars=stars,
        words_learned=profile.get("words_learned", 0),
        today_practice_minutes=minutes,
        streak_days=profile.get("streak_days", 1),
        current_level=level,
        badges=badges
    )

@router.post("/practice/record")
def record_baby_practice(req: PracticeProgressRequest):
    """Ghi nhận bé vừa hoàn thành luyện tập một từ hoặc bài học"""
    result = record_practice(
        item_id=req.item_id,
        age_group=req.age_group,
        category=req.category or "general",
        stars=req.stars_earned,
        duration_seconds=req.duration_seconds
    )
    return {"status": "success", "updated_stats": result}

@router.post("/speech/evaluate", response_model=SpeechEvaluateResponse)
def evaluate_speech(req: SpeechEvaluateRequest):
    """
    Đánh giá phát âm của bé dựa trên nhận diện giọng nói.
    Thiết kế tâm lý đặc thù cho trẻ em mầm non:
    - Trẻ 2 tuổi: Chỉ cần bật âm gần giống hoặc có nỗ lực nói là được khen thưởng tối đa 3 sao.
    - Trẻ 3-5 tuổi: Chấm điểm tương đồng nhưng luôn tràn đầy khích lệ, tuyệt đối không chê bé.
    """
    target_clean = normalize_text(req.target_text)
    spoken_clean = normalize_text(req.spoken_text)

    # Tính toán độ khớp tương đối
    matcher = difflib.SequenceMatcher(None, target_clean, spoken_clean)
    ratio = matcher.ratio()

    # Kiểm tra xem từ mục tiêu có nằm trọn trong chuỗi bé nói không
    is_contained = target_clean in spoken_clean or spoken_clean in target_clean

    # Điều chỉnh độ nhạy theo lứa tuổi
    if req.age_group == "age_2":
        # Với bé 2 tuổi, bé chỉ cần phát âm được 1 từ con hoặc âm gần giống là đạt
        score = int(ratio * 100)
        if is_contained or ratio >= 0.4 or len(spoken_clean) >= 2:
            score = max(score, 90)
            stars = 3
            feedback = "Hoan hô bé yêu! Bé bật âm giỏi quá chừng! 🎉"
            audio_text = "Hoan hô bé yêu! Bé giỏi quá!"
            is_match = True
        else:
            score = max(score, 75)
            stars = 2
            feedback = "Bé cố gắng rất tốt! Cùng cô nói to lại lần nữa nào! 👏"
            audio_text = "Bé nói hay lắm, làm lại lần nữa nào!"
            is_match = False
    else:
        # Với bé 3, 4, 5 tuổi
        score = int(ratio * 100)
        if is_contained:
            score = max(score, 95)

        if score >= 80:
            stars = 3
            feedback = "Tuyệt vời lắm bé ơi! Bé phát âm chuẩn và to rõ ràng! 🌟"
            audio_text = "Tuyệt vời! Bé phát âm rất chuẩn!"
            is_match = True
        elif score >= 50:
            stars = 2
            feedback = "Bé nói gần đúng rồi đó! Thử lại một lần nữa thật to nhé! 💪"
            audio_text = "Bé giỏi lắm, thử lại một lần nữa nào!"
            is_match = True
        else:
            stars = 1
            feedback = "Bé yêu nghe lại cô đọc mẫu rồi nói theo cô nhé! Cố lên nào! ❤️"
            audio_text = "Bé nghe lại rồi nói theo cô nhé!"
            is_match = False

    # Lưu lại lịch sử luyện phát âm
    save_speech_record(
        target=req.target_text,
        spoken=req.spoken_text,
        score=score,
        stars=stars,
        age_group=req.age_group
    )

    return SpeechEvaluateResponse(
        is_match=is_match,
        score=score,
        stars=stars,
        feedback=feedback,
        encouragement_audio=audio_text,
        target_text=req.target_text,
        spoken_text=req.spoken_text
    )

@router.get("/badges")
def get_badges():
    """Lấy danh sách các huy hiệu của bé"""
    return {"status": "success", "badges": get_badges_list()}

@router.get("/settings")
def get_app_settings():
    """Lấy cài đặt người dùng"""
    return {"status": "success", "settings": get_settings()}

@router.post("/settings")
def save_app_settings(settings: SettingsUpdate):
    """Lưu cài đặt người dùng"""
    if settings.voice_accent is not None:
        update_setting("voice_accent", settings.voice_accent)
    if settings.eye_care_minutes is not None:
        update_setting("eye_care_minutes", str(settings.eye_care_minutes))
    if settings.sound_effects is not None:
        update_setting("sound_effects", "true" if settings.sound_effects else "false")
    if settings.bg_music is not None:
        update_setting("bg_music", "true" if settings.bg_music else "false")
    return {"status": "success", "message": "Đã lưu cài đặt thành công!"}
