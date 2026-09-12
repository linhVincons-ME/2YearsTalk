"""
Ngân hàng dữ liệu giáo trình Bé Tập Nói Tiếng Việt (Ages 2-5)
Biên soạn theo tiêu chuẩn Montessori, Âm ngữ trị liệu và Chương trình Giáo dục Mầm non Việt Nam.
"""

CURRICULUM_DATA = {
    # =========================================================================
    # LỚP 2 TUỔI: BẬT ÂM, TỪ ĐƠN, TỪ ĐÔI, NHẬN BIẾT & GỌI TÊN
    # =========================================================================
    "age_2": {
        "title": "Lớp Mầm Nhỏ (2 Tuổi)",
        "stage": "Bật Âm & Từ Đơn / Đôi Đầu Đời",
        "description": "Kích thích bé bắt chước âm thanh, gọi tên người thân, bày tỏ nhu cầu thiết yếu và làm quen các cử chỉ lễ phép.",
        "milestones": [
            "Bắt chước âm thanh con vật, xe cộ quen thuộc",
            "Nói được từ đơn rõ ràng (Ba, Mẹ, Bà, Đi, Ăn)",
            "Bắt đầu ghép từ đôi (Uống nước, Đi chơi, Ba bế)",
            "Biết gật đầu, dạ, vâng, ạ khi được gọi tên"
        ],
        "categories": [
            {
                "id": "animal_sounds",
                "name": "Tiếng Kêu Con Vật",
                "icon": "🐶",
                "color": "#FF7675",
                "items": [
                    {
                        "id": "dog",
                        "word": "Con Chó",
                        "sound_text": "Gâu gâu",
                        "phonetic": "c-on ch-ó, g-âu g-âu",
                        "sentence": "Con chó kêu gâu gâu",
                        "mouth_guide": "Bé mở miệng tròn rồi khép lại nhẹ: gâu gâu",
                        "icon": "🐕",
                        "bg_color": "#FFEAA7",
                        "badge": "Âm thanh vui nhộn"
                    },
                    {
                        "id": "cat",
                        "word": "Con Mèo",
                        "sound_text": "Meo meo",
                        "phonetic": "c-on m-èo, m-eo m-eo",
                        "sentence": "Con mèo kêu meo meo",
                        "mouth_guide": "Bé mím môi lại rồi mở ra kêu: meo meo",
                        "icon": "🐱",
                        "bg_color": "#FAB1A0",
                        "badge": "Âm thanh vui nhộn"
                    },
                    {
                        "id": "duck",
                        "word": "Con Vịt",
                        "sound_text": "Cạp cạp",
                        "phonetic": "c-on v-ịt, c-ạp c-ạp",
                        "sentence": "Con vịt kêu cạp cạp",
                        "mouth_guide": "Bé mở to miệng phát âm dứt khoát: cạp cạp",
                        "icon": "🦆",
                        "bg_color": "#55EFC4",
                        "badge": "Âm thanh vui nhộn"
                    },
                    {
                        "id": "rooster",
                        "word": "Gà Trống",
                        "sound_text": "Ò ó o",
                        "phonetic": "g-à tr-ống, ò ó o",
                        "sentence": "Gà trống gáy ò ó o",
                        "mouth_guide": "Bé ngân dài giọng vui vẻ: ò ó o",
                        "icon": "🐓",
                        "bg_color": "#FD79A8",
                        "badge": "Âm thanh vui nhộn"
                    },
                    {
                        "id": "cow",
                        "word": "Con Bò",
                        "sound_text": "Ùm bò",
                        "phonetic": "c-on b-ò, ù-m b-ò",
                        "sentence": "Con bò kêu ùm bò",
                        "mouth_guide": "Bé ngân âm trầm sâu: ùm bò",
                        "icon": "🐄",
                        "bg_color": "#81ECEC",
                        "badge": "Âm thanh vui nhộn"
                    },
                    {
                        "id": "car",
                        "word": "Xe Ô Tô",
                        "sound_text": "Bim bim",
                        "phonetic": "x-e ô t-ô, b-im b-im",
                        "sentence": "Còi xe kêu bim bim",
                        "mouth_guide": "Bé mím hai môi bật mạnh: bim bim",
                        "icon": "🚗",
                        "bg_color": "#74B9FF",
                        "badge": "Phương tiện"
                    }
                ]
            },
            {
                "id": "family",
                "name": "Người Thân Yêu",
                "icon": "👨‍👩‍👧",
                "color": "#FD79A8",
                "items": [
                    {
                        "id": "ba",
                        "word": "Ba",
                        "sound_text": "Ba ơi",
                        "phonetic": "b-a",
                        "sentence": "Bé yêu Ba nhiều",
                        "mouth_guide": "Mím chặt hai môi rồi bật hơi ra: Ba",
                        "icon": "👨",
                        "bg_color": "#DFE6E9",
                        "badge": "Gia đình"
                    },
                    {
                        "id": "me",
                        "word": "Mẹ",
                        "sound_text": "Mẹ ơi",
                        "phonetic": "m-ẹ",
                        "sentence": "Mẹ yêu thương bé",
                        "mouth_guide": "Mím môi, giọng ngân ấm áp: Mẹ",
                        "icon": "👩",
                        "bg_color": "#FAB1A0",
                        "badge": "Gia đình"
                    },
                    {
                        "id": "ong",
                        "word": "Ông",
                        "sound_text": "Ông ơi",
                        "phonetic": "ô-ng",
                        "sentence": "Bé chào Ông ạ",
                        "mouth_guide": "Tròn môi đẩy hơi: Ông",
                        "icon": "👴",
                        "bg_color": "#A29BFE",
                        "badge": "Gia đình"
                    },
                    {
                        "id": "ba_noi",
                        "word": "Bà",
                        "sound_text": "Bà ơi",
                        "phonetic": "b-à",
                        "sentence": "Bà ru bé ngủ",
                        "mouth_guide": "Bật môi nhẹ giọng trầm: Bà",
                        "icon": "👵",
                        "bg_color": "#FFEAA7",
                        "badge": "Gia đình"
                    },
                    {
                        "id": "be",
                        "word": "Bé Ngoan",
                        "sound_text": "Bé ngoan",
                        "phonetic": "b-é ng-oan",
                        "sentence": "Bé là em bé ngoan",
                        "mouth_guide": "Bật môi cười tươi: Bé",
                        "icon": "👶",
                        "bg_color": "#55EFC4",
                        "badge": "Bé yêu"
                    }
                ]
            },
            {
                "id": "daily_needs",
                "name": "Nhu Cầu Hàng Ngày",
                "icon": "🍼",
                "color": "#0984E3",
                "items": [
                    {
                        "id": "water",
                        "word": "Uống Nước",
                        "sound_text": "Uống nước",
                        "phonetic": "u-ống n-ước",
                        "sentence": "Con muốn uống nước",
                        "mouth_guide": "Mở tròn môi: Uống nước",
                        "icon": "💧",
                        "bg_color": "#74B9FF",
                        "badge": "Nhu cầu"
                    },
                    {
                        "id": "eat",
                        "word": "Ăn Cơm",
                        "sound_text": "Ăn cơm",
                        "phonetic": "ă-n c-ơm",
                        "sentence": "Bé ngồi ăn cơm",
                        "mouth_guide": "Cười mở miệng: Ăn cơm",
                        "icon": "🍚",
                        "bg_color": "#FFEAA7",
                        "badge": "Nhu cầu"
                    },
                    {
                        "id": "milk",
                        "word": "Bình Sữa",
                        "sound_text": "Sữa thơm",
                        "phonetic": "b-ình s-ữa",
                        "sentence": "Bé uống bình sữa",
                        "mouth_guide": "Cong lưỡi nhẹ âm S: Sữa",
                        "icon": "🍼",
                        "bg_color": "#DFE6E9",
                        "badge": "Nhu cầu"
                    },
                    {
                        "id": "sleep",
                        "word": "Đi Ngủ",
                        "sound_text": "Ngủ ngon",
                        "phonetic": "đ-i ng-ủ",
                        "sentence": "Bé nhắm mắt đi ngủ",
                        "mouth_guide": "Đầu lưỡi chạm răng trên: Đi, rồi khép: Ngủ",
                        "icon": "🛏️",
                        "bg_color": "#A29BFE",
                        "badge": "Nhu cầu"
                    },
                    {
                        "id": "carry",
                        "word": "Bế Con",
                        "sound_text": "Mẹ bế con",
                        "phonetic": "b-ế c-on",
                        "sentence": "Mẹ ơi bế con với",
                        "mouth_guide": "Hai môi bật hơi: Bế",
                        "icon": "🤱",
                        "bg_color": "#FD79A8",
                        "badge": "Nhu cầu"
                    }
                ]
            },
            {
                "id": "body_parts",
                "name": "Bộ Phận Cơ Thể",
                "icon": "👀",
                "color": "#00B894",
                "items": [
                    {
                        "id": "eyes",
                        "word": "Đôi Mắt",
                        "sound_text": "Mắt xinh",
                        "phonetic": "đ-ôi m-ắt",
                        "sentence": "Đôi mắt bé chớp chớp",
                        "mouth_guide": "Khép môi rồi mở nhanh: Mắt",
                        "icon": "👁️",
                        "bg_color": "#81ECEC",
                        "badge": "Cơ thể"
                    },
                    {
                        "id": "nose",
                        "word": "Cái Mũi",
                        "sound_text": "Mũi xinh",
                        "phonetic": "c-ái m-ũi",
                        "sentence": "Cái mũi bé hít hà",
                        "mouth_guide": "Nhấn giọng dấu ngã: Mũi",
                        "icon": "👃",
                        "bg_color": "#FAB1A0",
                        "badge": "Cơ thể"
                    },
                    {
                        "id": "mouth",
                        "word": "Cái Miệng",
                        "sound_text": "Miệng cười",
                        "phonetic": "c-ái m-iệng",
                        "sentence": "Cái miệng cười toe toét",
                        "mouth_guide": "Kéo dài mép cười: Miệng",
                        "icon": "👄",
                        "bg_color": "#FF7675",
                        "badge": "Cơ thể"
                    },
                    {
                        "id": "ears",
                        "word": "Cái Tai",
                        "sound_text": "Tai lắng nghe",
                        "phonetic": "c-ái t-ai",
                        "sentence": "Cái tai nghe tiếng chim hót",
                        "mouth_guide": "Đầu lưỡi chạm răng trên: Tai",
                        "icon": "👂",
                        "bg_color": "#FFEAA7",
                        "badge": "Cơ thể"
                    },
                    {
                        "id": "hands",
                        "word": "Đôi Tay",
                        "sound_text": "Tay ngoan",
                        "phonetic": "đ-ôi t-ay",
                        "sentence": "Đôi tay vỗ vỗ hoan hô",
                        "mouth_guide": "Bật hơi đầu lưỡi: Tay",
                        "icon": "🙌",
                        "bg_color": "#55EFC4",
                        "badge": "Cơ thể"
                    }
                ]
            }
        ]
    },

    # =========================================================================
    # LỚP 3 TUỔI: CÂU NGẮN 3-5 TỪ, MÀU SẮC, HÌNH KHỐI, HÀNH ĐỘNG
    # =========================================================================
    "age_3": {
        "title": "Lớp Mầm Lớn (3 Tuổi)",
        "stage": "Câu Ngắn & Khám Phá Thế Giới Xung Quanh",
        "description": "Bé nói câu 3-5 từ mạch lạc, nhận biết màu sắc, phân biệt đồ vật, cảm xúc và sửa các lỗi ngọng phụ âm đầu.",
        "milestones": [
            "Nói được câu đầy đủ: Chủ ngữ + Động từ + Vị ngữ",
            "Nhận biết 5+ màu sắc cơ bản và hình khối tròn, vuông",
            "Biết trả lời câu hỏi 'Đây là cái gì?' và 'Ai đây?'",
            "Phát âm phân biệt rõ B - P, Đ - D, L - N"
        ],
        "categories": [
            {
                "id": "colors_shapes",
                "name": "Màu Sắc & Hình Khối",
                "icon": "🎨",
                "color": "#E17055",
                "items": [
                    {
                        "id": "red",
                        "word": "Màu Đỏ",
                        "sentence": "Quả dâu tây màu đỏ tươi",
                        "sound_text": "Màu đỏ rực rỡ",
                        "phonetic": "m-àu đ-ỏ",
                        "icon": "🍓",
                        "bg_color": "#FF7675",
                        "badge": "Màu sắc"
                    },
                    {
                        "id": "yellow",
                        "word": "Màu Vàng",
                        "sentence": "Bông hoa hướng dương màu vàng",
                        "sound_text": "Màu vàng tươi",
                        "phonetic": "m-àu v-àng",
                        "icon": "🌻",
                        "bg_color": "#FFEAA7",
                        "badge": "Màu sắc"
                    },
                    {
                        "id": "green",
                        "word": "Màu Xanh Lá",
                        "sentence": "Chiếc lá cây màu xanh lá mát",
                        "sound_text": "Xanh lá cây",
                        "phonetic": "m-àu x-anh l-á",
                        "icon": "🍃",
                        "bg_color": "#55EFC4",
                        "badge": "Màu sắc"
                    },
                    {
                        "id": "blue",
                        "word": "Màu Xanh Dương",
                        "sentence": "Bầu trời bao la màu xanh dương",
                        "sound_text": "Xanh da trời",
                        "phonetic": "m-àu x-anh d-ương",
                        "icon": "🌊",
                        "bg_color": "#74B9FF",
                        "badge": "Màu sắc"
                    },
                    {
                        "id": "circle",
                        "word": "Hình Tròn",
                        "sentence": "Ông mặt trời tròn vo chiếu sáng",
                        "sound_text": "Hình tròn xoe",
                        "phonetic": "h-ình tr-òn",
                        "icon": "🔴",
                        "bg_color": "#FAB1A0",
                        "badge": "Hình khối"
                    },
                    {
                        "id": "square",
                        "word": "Hình Vuông",
                        "sentence": "Chiếc bánh chưng có hình vuông vức",
                        "sound_text": "Hình vuông",
                        "phonetic": "h-ình v-uông",
                        "icon": "🟩",
                        "bg_color": "#81ECEC",
                        "badge": "Hình khối"
                    }
                ]
            },
            {
                "id": "sentence_building",
                "name": "Bé Ghép Câu Hoàn Chỉnh",
                "icon": "🧩",
                "color": "#6C5CE7",
                "items": [
                    {
                        "id": "s_want_apple",
                        "word": "Con muốn ăn táo",
                        "sentence": "Con muốn ăn quả táo đỏ ngọt",
                        "sound_text": "Con muốn ăn táo",
                        "tokens": ["Con", "muốn", "ăn", "táo"],
                        "icon": "🍎",
                        "bg_color": "#FF7675",
                        "badge": "Nói trọn câu"
                    },
                    {
                        "id": "s_mom_hug",
                        "word": "Mẹ ơi bế con",
                        "sentence": "Mẹ ơi hãy bế con với",
                        "sound_text": "Mẹ ơi bế con",
                        "tokens": ["Mẹ", "ơi", "bế", "con"],
                        "icon": "🤱",
                        "bg_color": "#FD79A8",
                        "badge": "Nói trọn câu"
                    },
                    {
                        "id": "s_dad_home",
                        "word": "Ba đi làm về",
                        "sentence": "Hoan hô ba đã đi làm về",
                        "sound_text": "Ba đi làm về",
                        "tokens": ["Ba", "đi", "làm", "về"],
                        "icon": "💼",
                        "bg_color": "#74B9FF",
                        "badge": "Nói trọn câu"
                    },
                    {
                        "id": "s_brush_teeth",
                        "word": "Bé tự đánh răng",
                        "sentence": "Mỗi sáng bé tự đánh răng sạch",
                        "sound_text": "Bé tự đánh răng",
                        "tokens": ["Bé", "tự", "đánh", "răng"],
                        "icon": "🪥",
                        "bg_color": "#55EFC4",
                        "badge": "Kỹ năng sống"
                    },
                    {
                        "id": "s_play_ball",
                        "word": "Bạn thỏ đá bóng",
                        "sentence": "Bạn thỏ cùng đá bóng vui vẻ",
                        "sound_text": "Bạn thỏ đá bóng",
                        "tokens": ["Bạn", "thỏ", "đá", "bóng"],
                        "icon": "⚽",
                        "bg_color": "#FFEAA7",
                        "badge": "Nói trọn câu"
                    }
                ]
            },
            {
                "id": "emotions",
                "name": "Cảm Xúc Của Bé",
                "icon": "😊",
                "color": "#FDCB6E",
                "items": [
                    {
                        "id": "happy",
                        "word": "Bé Rất Vui",
                        "sentence": "Hôm nay bé được đi chơi vui lắm",
                        "sound_text": "Bé rất vui",
                        "icon": "😄",
                        "bg_color": "#FFEAA7",
                        "badge": "Cảm xúc"
                    },
                    {
                        "id": "love",
                        "word": "Yêu Thương",
                        "sentence": "Bé yêu ông bà, cha mẹ nhất trần đời",
                        "sound_text": "Yêu thương cả nhà",
                        "icon": "❤️",
                        "bg_color": "#FD79A8",
                        "badge": "Cảm xúc"
                    },
                    {
                        "id": "tired",
                        "word": "Bé Buồn Ngủ",
                        "sentence": "Bé ngáp to, bé buồn ngủ rồi ạ",
                        "sound_text": "Bé buồn ngủ",
                        "icon": "🥱",
                        "bg_color": "#A29BFE",
                        "badge": "Cảm xúc"
                    },
                    {
                        "id": "proud",
                        "word": "Bé Ngoan Ngoãn",
                        "sentence": "Bé biết vâng lời, ba mẹ khen ngợi",
                        "sound_text": "Bé rất ngoan",
                        "icon": "⭐",
                        "bg_color": "#55EFC4",
                        "badge": "Cảm xúc"
                    }
                ]
            }
        ]
    },

    # =========================================================================
    # LỚP 4 TUỔI: ĐỒNG DAO, THƠ CA, KỂ CHUYỆN & CÂU PHỨC
    # =========================================================================
    "age_4": {
        "title": "Lớp Chồi (4 Tuổi)",
        "stage": "Đồng Dao, Kể Chuyện & Phản Xạ Giao Tiếp",
        "description": "Luyện nhịp điệu qua các bài đồng dao truyền thống, tập kể chuyện theo tranh 3-4 cảnh và rèn luyện phản xạ đối thoại linh hoạt.",
        "milestones": [
            "Đọc thuộc các bài đồng dao ca dao thiếu nhi ngắn",
            "Biết dùng từ nối diễn đạt lý do: 'vì... nên', 'tại sao', 'ở đâu'",
            "Kể lại được nội dung câu chuyện ngắn 3-4 bức tranh",
            "Tự tin chào hỏi, xin phép, cảm ơn và xin lỗi đúng lúc"
        ],
        "rhymes": [
            {
                "id": "dung_dang",
                "title": "Dung Dăng Dung Dẻ",
                "icon": "👭",
                "description": "Bài đồng dao giúp bé luyện nhịp điệu, bật hơi vui tươi và bước đều.",
                "lines": [
                    "Dung dăng dung dẻ",
                    "Dắt trẻ đi chơi",
                    "Đến ngõ nhà trời",
                    "Lạy cậu lạy mợ",
                    "Cho cháu về quê",
                    "Cho dê đi học",
                    "Cho cóc ở nhà",
                    "Cho gà bới bếp",
                    "Xì xà xì xụp",
                    "Ngồi thụp xuống đây!"
                ]
            },
            {
                "id": "keo_cua",
                "title": "Kéo Cưa Lừa Xẻ",
                "icon": "🪵",
                "description": "Rèn luyện nhịp thở đều đặn và sự dứt khoát của các âm thanh.",
                "lines": [
                    "Kéo cưa lừa xẻ",
                    "Ông thợ nào khỏe",
                    "Về ăn cơm vua",
                    "Ông thợ nào thua",
                    "Về bú tí mẹ!"
                ]
            },
            {
                "id": "nu_na",
                "title": "Nu Na Nu Nống",
                "icon": "🦶",
                "description": "Trò chơi đếm ngón chân gõ nhịp quen thuộc rộn rã tiếng cười.",
                "lines": [
                    "Nu na nu nống",
                    "Đánh trống phất cờ",
                    "Mở cuộc thi đua",
                    "Chân ai sạch sẽ",
                    "Gót đỏ hồng hào",
                    "Không bẩn tí nào",
                    "Được vào đánh trống!"
                ]
            },
            {
                "id": "tap_tam_vong",
                "title": "Tập Tầm Vông",
                "icon": "✊",
                "description": "Luyện khả năng phán đoán, phân biệt tay có tay không.",
                "lines": [
                    "Tập tầm vông",
                    "Tay không tay có",
                    "Tập tầm vó",
                    "Tay có tay không",
                    "Tay nào có?",
                    "Tay nào không?"
                ]
            }
        ],
        "stories": [
            {
                "id": "rabbit_obey",
                "title": "Chú Thỏ Con Vâng Lời",
                "icon": "🐰",
                "summary": "Câu chuyện dạy bé biết nghe lời mẹ dặn khi ra ngoài chơi.",
                "scenes": [
                    {
                        "step": 1,
                        "image_icon": "🏡",
                        "text": "Thỏ mẹ dặn: Thỏ con ngoan ngoãn chơi gần nhà, đừng đi xa nhé!",
                        "prompt": "Thỏ mẹ đã dặn thỏ con điều gì?"
                    },
                    {
                        "step": 2,
                        "image_icon": "🦋",
                        "text": "Bạn Bươm Bướm rủ: Thỏ ơi, ngoài đồng hoa đẹp lắm, đi chơi đi!",
                        "prompt": "Ai đã rủ thỏ con chạy đi xa?"
                    },
                    {
                        "step": 3,
                        "image_icon": "🌲",
                        "text": "Thỏ mải đuổi bướm nên bị lạc vào rừng sâu, thỏ ngồi khóc hu hu.",
                        "prompt": "Vì sao thỏ con bị lạc và khóc?"
                    },
                    {
                        "step": 4,
                        "image_icon": "🐻",
                        "text": "Bác Gấu tốt bụng dẫn thỏ về nhà. Thỏ xin lỗi mẹ và hứa vâng lời.",
                        "prompt": "Bác Gấu đã giúp thỏ con như thế nào?"
                    }
                ]
            },
            {
                "id": "turtle_hare",
                "title": "Rùa Và Thỏ Chạy Thi",
                "icon": "🐢",
                "summary": "Bài học kiên trì, không tự kiêu dành cho bé yêu.",
                "scenes": [
                    {
                        "step": 1,
                        "image_icon": "🏁",
                        "text": "Thỏ khoe khoang chạy nhanh, thách thức bác Rùa chạy thi xem ai thắng.",
                        "prompt": "Thỏ đã thách đố bác Rùa điều gì?"
                    },
                    {
                        "step": 2,
                        "image_icon": "🌳",
                        "text": "Nghĩ mình chạy nhanh hơn, Thỏ thong thả nằm ngủ gật dưới gốc cây to.",
                        "prompt": "Thỏ đã làm gì khi đang thi chạy?"
                    },
                    {
                        "step": 3,
                        "image_icon": "🐢",
                        "text": "Bác Rùa chậm chạp nhưng chăm chỉ từng bước kiên trì tiến về phía trước.",
                        "prompt": "Bác Rùa thi chạy như thế nào?"
                    },
                    {
                        "step": 4,
                        "image_icon": "🏆",
                        "text": "Khi Thỏ tỉnh giấc thì bác Rùa đã tới đích rồi! Rùa giành chiến thắng vẻ vang.",
                        "prompt": "Cuối cùng ai là người chiến thắng?"
                    }
                ]
            }
        ]
    },

    # =========================================================================
    # LỚP 5 TUỔI: TIỀN TIỂU HỌC, 6 THANH ĐIỆU, 29 CHỮ CÁI & GHÉP VẦN
    # =========================================================================
    "age_5": {
        "title": "Lớp Lá / Tiền Tiểu Học (5 Tuổi)",
        "stage": "Chuẩn Thanh Điệu, 29 Chữ Cái & Ghép Vần Kỳ Diệu",
        "description": "Làm quen toàn bộ 29 chữ cái tiếng Việt, phân biệt chuẩn 6 thanh điệu (sắc, huyền, hỏi, ngã, nặng) và cỗ xe ghép vần trực quan.",
        "milestones": [
            "Thuộc bảng chữ cái 29 chữ tiếng Việt và phát âm chính xác",
            "Phân biệt rõ 6 thanh điệu, đặc biệt không nhầm ngã và hỏi",
            "Biết ghép phụ âm + nguyên âm + thanh điệu đơn giản (b-a -> ba, bà, bá...)",
            "Giải được các câu đố dân gian vui tươi, kích thích trí não"
        ],
        "tones": [
            {
                "id": "tone_none",
                "name": "Thanh Ngang (Không dấu)",
                "symbol": "—",
                "motion": "Đường bằng phẳng nhẹ nhàng",
                "example": "Ba, Ca, Ma, Hoa",
                "guide": "Giữ giọng đều, nhẹ nhàng như xe chạy đường bằng.",
                "color": "#74B9FF"
            },
            {
                "id": "tone_sac",
                "name": "Thanh Sắc",
                "symbol": "／",
                "motion": "Đang leo dốc núi lên cao",
                "example": "Bá, Cá, Má, Hóa",
                "guide": "Lên giọng cao vút như máy bay cất cánh lên trời.",
                "color": "#FF7675"
            },
            {
                "id": "tone_huyen",
                "name": "Thanh Huyền",
                "symbol": "＼",
                "motion": "Trượt dốc êm ái xuống thấp",
                "example": "Bà, Cà, Mà, Hòa",
                "guide": "Hạ giọng trầm xuống nhẹ nhàng như trượt cầu tuột.",
                "color": "#55EFC4"
            },
            {
                "id": "tone_hoi",
                "name": "Thanh Hỏi",
                "symbol": "ˀ",
                "motion": "Vòng cung lượn xuống rồi móc lên",
                "example": "Bả, Cả, Mả, Hỏa",
                "guide": "Giọng hơi cong xuống rồi nhấc nhẹ lên.",
                "color": "#FDCB6E"
            },
            {
                "id": "tone_nga",
                "name": "Thanh Ngã",
                "symbol": "～",
                "motion": "Sóng lượn nhấp nhô gấp khúc",
                "example": "Bã, Cã, Mã, Hõa",
                "guide": "Lên giọng, ngắt nhẹ giữa chừng rồi ngân vang.",
                "color": "#FD79A8"
            },
            {
                "id": "tone_nang",
                "name": "Thanh Nặng",
                "symbol": "•",
                "motion": "Dấu chấm dứt khoát sâu lắng",
                "example": "Bạ, Cạ, Mạ, Họa",
                "guide": "Hạ giọng thật sâu và dứt khoát ngay tại chỗ.",
                "color": "#A29BFE"
            }
        ],
        "alphabet": [
            {"letter": "A", "sound": "a", "word": "Quả Cam", "icon": "🍊"},
            {"letter": "Ă", "sound": "á", "word": "Mặt Trăng", "icon": "🌙"},
            {"letter": "Â", "sound": "ớ", "word": "Cây Nấm", "icon": "🍄"},
            {"letter": "B", "sound": "bờ", "word": "Quả Bóng", "icon": "⚽"},
            {"letter": "C", "sound": "cờ", "word": "Con Cá", "icon": "🐟"},
            {"letter": "D", "sound": "dờ", "word": "Quả Dưa", "icon": "🍉"},
            {"letter": "Đ", "sound": "đờ", "word": "Đồng Hồ", "icon": "⏰"},
            {"letter": "E", "sound": "e", "word": "Em Bé", "icon": "👶"},
            {"letter": "Ê", "sound": "ê", "word": "Con Búp Bê", "icon": "🎎"},
            {"letter": "G", "sound": "gờ", "word": "Gà Trống", "icon": "🐓"},
            {"letter": "H", "sound": "hờ", "word": "Bông Hoa", "icon": "🌸"},
            {"letter": "I", "sound": "i", "word": "Hòn Bi", "icon": "🔮"},
            {"letter": "K", "sound": "ca", "word": "Cái Kéo", "icon": "✂️"},
            {"letter": "L", "sound": "lờ", "word": "Chiếc Lá", "icon": "🍃"},
            {"letter": "M", "sound": "mờ", "word": "Quả Mận", "icon": "🫐"},
            {"letter": "N", "sound": "nờ", "word": "Cái Nơ", "icon": "🎀"},
            {"letter": "O", "sound": "o", "word": "Con Ong", "icon": "🐝"},
            {"letter": "Ô", "sound": "ô", "word": "Chiếc Ô", "icon": "☂️"},
            {"letter": "Ơ", "sound": "ơ", "word": "Lá Cờ", "icon": "🚩"},
            {"letter": "P", "sound": "pờ", "word": "Đèn Pin", "icon": "🔦"},
            {"letter": "Q", "sound": "quy", "word": "Quạt Mát", "icon": "🪭"},
            {"letter": "R", "sound": "rờ", "word": "Con Rùa", "icon": "🐢"},
            {"letter": "S", "sound": "sờ", "word": "Ngôi Sao", "icon": "⭐"},
            {"letter": "T", "sound": "tờ", "word": "Tàu Hỏa", "icon": "🚂"},
            {"letter": "U", "sound": "u", "word": "Cái Mũ", "icon": "🧢"},
            {"letter": "Ư", "sound": "ư", "word": "Con Sư Tử", "icon": "🦁"},
            {"letter": "V", "sound": "vờ", "word": "Con Vịt", "icon": "🦆"},
            {"letter": "X", "sound": "xờ", "word": "Xe Đạp", "icon": "🚲"},
            {"letter": "Y", "sound": "y dài", "word": "Y tá", "icon": "👩‍⚕️"}
        ],
        "blending_lessons": [
            {
                "consonant": "B",
                "vowel": "A",
                "base": "BA",
                "variations": [
                    {"word": "BA", "tone": "Thanh Ngang", "meaning": "Ba của bé yêu quý", "icon": "👨"},
                    {"word": "BÀ", "tone": "Thanh Huyền", "meaning": "Bà hiền hậu kể chuyện", "icon": "👵"},
                    {"word": "BÁ", "tone": "Thanh Sắc", "meaning": "Bác ruột trong nhà", "icon": "👤"},
                    {"word": "BẢ", "tone": "Thanh Hỏi", "meaning": "Bả mồi thơm phức", "icon": "🎣"},
                    {"word": "BÃ", "tone": "Thanh Ngã", "meaning": "Bã mía ngọt thơm", "icon": "🎋"},
                    {"word": "BẠ", "tone": "Thanh Nặng", "meaning": "Bạn bè cùng lớp", "icon": "👫"}
                ]
            },
            {
                "consonant": "C",
                "vowel": "A",
                "base": "CA",
                "variations": [
                    {"word": "CA", "tone": "Thanh Ngang", "meaning": "Bé thích hát ca", "icon": "🎤"},
                    {"word": "CÀ", "tone": "Thanh Huyền", "meaning": "Quả cà tím ngon lành", "icon": "🍆"},
                    {"word": "CÁ", "tone": "Thanh Sắc", "meaning": "Con cá bơi dưới nước", "icon": "🐟"},
                    {"word": "CẢ", "tone": "Thanh Hỏi", "meaning": "Cả nhà cùng quây quần", "icon": "👨‍👩‍👧"},
                    {"word": "CẠ", "tone": "Thanh Nặng", "meaning": "Cọ cọ cạ vào nhau", "icon": "🤝"}
                ]
            },
            {
                "consonant": "M",
                "vowel": "E",
                "base": "ME",
                "variations": [
                    {"word": "ME", "tone": "Thanh Ngang", "meaning": "Quả me chua ngọt", "icon": "🫘"},
                    {"word": "MÈ", "tone": "Thanh Huyền", "meaning": "Hạt vừng hạt mè thơm", "icon": "🌾"},
                    {"word": "MÉ", "tone": "Thanh Sắc", "meaning": "Bên mé sông nước chảy", "icon": "🏞️"},
                    {"word": "MẺ", "tone": "Thanh Hỏi", "meaning": "Một mẻ bánh thơm lừng", "icon": "🍪"},
                    {"word": "MẸ", "tone": "Thanh Nặng", "meaning": "Mẹ hiền chăm sóc bé", "icon": "👩"}
                ]
            }
        ],
        "riddles": [
            {
                "id": "rid_1",
                "question": "Con gì đuôi ngắn tai dài, mắt hồng lông mượt có tài nhảy nhanh?",
                "answer": "Con Thỏ",
                "options": ["Con Thỏ", "Con Rùa", "Con Chó", "Con Mèo"],
                "explanation": "Đúng rồi! Bạn Thỏ có đôi tai dài và chạy rất nhanh!",
                "icon": "🐰"
            },
            {
                "id": "rid_2",
                "question": "Cái gì lấp lánh ban đêm, cùng trăng soi sáng dịu êm bầu trời?",
                "answer": "Ngôi Sao",
                "options": ["Mặt Trời", "Ngôi Sao", "Cái Đèn", "Chiếc Ô"],
                "explanation": "Bé giỏi lắm! Các ngôi sao lấp lánh cùng chú Cuội!",
                "icon": "⭐"
            },
            {
                "id": "rid_3",
                "question": "Con gì mào đỏ gáy vang, gọi ông mặt trời thức dậy đàng đông?",
                "answer": "Gà Trống",
                "options": ["Gà Mái", "Con Vịt", "Gà Trống", "Con Chim"],
                "explanation": "Tuyệt vời! Chú gà trống đánh thức mọi người dậy!",
                "icon": "🐓"
            }
        ]
    }
}

# CẨM NANG HƯỚNG DẪN DÀNH CHO PHỤ HUYNH & CHUYÊN GIA ÂM NGỮ TRỊ LIỆU
PARENTING_GUIDE = [
    {
        "id": "principle_1",
        "title": "Nguyên Tắc 'Tắm Ngôn Ngữ' Hàng Ngày",
        "category": "Phương Pháp Kích Hoạt",
        "icon": "🛁",
        "color": "#74B9FF",
        "summary": "Nói chuyện và tường thuật mọi hành động xung quanh một cách tự nhiên nhất.",
        "content": [
            "Hãy là 'bình luận viên' của con: Khi mẹ nấu cơm, mẹ rửa rau, ba gấp quần áo, hãy nói to thành lời để bé nghe và tích lũy vốn từ thụ động.",
            "Nói với nhịp độ chậm rãi, giọng điệu vui vẻ, khẩu hình mở rõ ràng ngang tầm mắt của con.",
            "Tập trung vào từ vựng then chốt: Nhấn mạnh các từ chỉ hành động (ăn, đi, lấy) và tên gọi đồ vật quen thuộc."
        ]
    },
    {
        "id": "principle_2",
        "title": "Quy Tắc 'Chờ 5 Giây' Thần Kỳ",
        "category": "Tương Tác Phản Xạ",
        "icon": "⏳",
        "color": "#FFEAA7",
        "summary": "Đừng vội đoán ý đưa ngay đồ chơi, hãy cho não bộ của bé thời gian xử lý và bật âm.",
        "content": [
            "Khi bé chỉ tay vào bình sữa hay món đồ chơi, cha mẹ hãy dừng lại 3 - 5 giây nhìn vào mắt con với vẻ chờ đợi khuyến khích.",
            "Gợi ý từ ngữ: 'Con muốn... sữa hả con? Sữa! Con nói: Sữa nào!'",
            "Chỉ cần bé phát ra bất kỳ âm thanh nào hoặc cố gắng nhại lại, hãy trao ngay món đồ và khen ngợi con nồng nhiệt!"
        ]
    },
    {
        "id": "principle_3",
        "title": "Kỹ Thuật 'Mở Rộng Câu +1 Từ'",
        "category": "Mở Rộng Vốn Từ",
        "icon": "➕",
        "color": "#55EFC4",
        "summary": "Tiếp nhận câu nói của con và thêm vào đúng 1 từ để nâng cấp phản xạ ngữ pháp.",
        "content": [
            "Nếu bé nói: 'Chó' -> Cha mẹ đáp: 'Đúng rồi, con chó to!' (thêm tính từ).",
            "Nếu bé nói: 'Uống' -> Cha mẹ đáp: 'Bé uống nước nhé!' (thêm danh từ).",
            "Nếu bé nói: 'Xe chạy' -> Cha mẹ đáp: 'Xe ô tô chạy nhanh ghê!'",
            "Cách này giúp bé không bị áp lực mà vốn câu dài dần một cách tự nhiên nhất."
        ]
    },
    {
        "id": "principle_4",
        "title": "Các Dấu Hiệu Cảnh Báo (Cờ Đỏ Chậm Nói Cần Can Thiệp)",
        "category": "Cảnh Báo Chuyên Gia",
        "icon": "🚩",
        "color": "#FF7675",
        "summary": "Nhận biết sớm các mốc phát triển để có can thiệp âm ngữ kịp thời.",
        "content": [
            "18 tháng: Chưa nói được từ đơn nào (ba, mẹ, bà), không quay đầu khi gọi tên, không biết chỉ tay vào thứ mình muốn.",
            "24 tháng: Vốn từ dưới 20 từ, chưa biết ghép từ đôi (ba bế, ăn cơm), chỉ thích dùng cử chỉ kéo tay người lớn.",
            "36 tháng: Không nói được câu 3 từ, người lạ không thể hiểu được bé nói gì, khó khăn khi giao tiếp mắt.",
            "LỜI KHUYÊN: Hãy cắt giảm tối đa tivi, điện thoại thụ động, tăng cường tương tác mặt đối mặt cùng con ít nhất 30-60 phút mỗi ngày."
        ]
    },
    {
        "id": "principle_5",
        "title": "Bài Tập Thể Dục Cơ Miệng & Phát Âm",
        "category": "Luyện Âm & Thể Lực Miệng",
        "icon": "👅",
        "color": "#FD79A8",
        "summary": "Giúp cơ môi, hàm và lưỡi của bé linh hoạt, nói rõ ràng không bị đớ lưỡi.",
        "content": [
            "Trò chơi thổi bong bóng xà phòng hoặc thổi chong chóng: Tăng cường luồng hơi và cơ tròn môi.",
            "Trò chơi liếm mép: Quệt chút sữa đặc quanh môi để bé dùng lưỡi liếm, giúp lưỡi mềm dẻo phát âm các âm L, N, T, Đ.",
            "Bắt chước âm thanh tặc lưỡi 'tách tách' như tiếng móng ngựa chạy.",
            "Cùng bé cười to, ngáp to, bĩu môi giả vờ làm mặt hề vui nhộn trước gương."
        ]
    }
]
