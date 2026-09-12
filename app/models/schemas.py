"""
Pydantic Schemas cho Bé Tập Nói (BeTapNoi)
"""
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class SpeechEvaluateRequest(BaseModel):
    target_text: str = Field(..., description="Từ hoặc câu mục tiêu bé cần nói")
    spoken_text: str = Field(..., description="Văn bản nhận diện được từ giọng bé nói")
    age_group: str = Field(..., description="Nhóm tuổi của bé: age_2, age_3, age_4, age_5")

class SpeechEvaluateResponse(BaseModel):
    is_match: bool
    score: int = Field(..., description="Điểm số chính xác từ 0 đến 100")
    stars: int = Field(..., description="Số sao thưởng: 1, 2 hoặc 3 sao")
    feedback: str = Field(..., description="Lời động viên ấm áp dành cho bé")
    encouragement_audio: str = Field(..., description="Gợi ý câu khích lệ phát âm")
    target_text: str
    spoken_text: str

class PracticeProgressRequest(BaseModel):
    age_group: str
    item_id: str
    category: Optional[str] = "general"
    stars_earned: int = 1
    duration_seconds: int = 30

class UserStats(BaseModel):
    total_stars: int = 0
    words_learned: int = 0
    today_practice_minutes: int = 0
    streak_days: int = 1
    current_level: str = "Bé Yêu Thông Thái"
    badges: List[Dict[str, Any]] = []

class SettingsUpdate(BaseModel):
    voice_accent: Optional[str] = "north"  # north (Bắc) hoặc south (Nam)
    eye_care_minutes: Optional[int] = 20   # Nhắc nghỉ ngơi sau 15, 20 hoặc 30 phút
    sound_effects: Optional[bool] = True
    bg_music: Optional[bool] = True
