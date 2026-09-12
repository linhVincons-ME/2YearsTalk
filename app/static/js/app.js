/**
 * app.js - Logic điều khiển giao diện chính của Bé Tập Nói (BeTapNoi)
 */

const AppState = {
    currentAge: 'age_2',
    currentSubView: 'flashcards',
    curriculumData: null,
    stats: {
        total_stars: 15,
        words_learned: 5,
        today_practice_minutes: 5,
        badges: []
    },
    voiceStudioTarget: null,
    eyeCareSeconds: 0,
    eyeCareMaxSeconds: 20 * 60, // 20 phút
    eyeCareTimerId: null
};

// ============================================================================
// Khởi Tạo Ứng Dụng
// ============================================================================
document.addEventListener('DOMContentLoaded', () => {
    initEventListeners();
    loadUserStats();
    loadAgeCurriculum('age_2');
    startEyeCareTimer();
});

function initEventListeners() {
    // Chuyển đổi tab lứa tuổi
    document.querySelectorAll('.age-tab').forEach(tab => {
        tab.addEventListener('click', (e) => {
            const ageKey = tab.dataset.age;
            if (ageKey && ageKey !== AppState.currentAge) {
                soundFx.playPop();
                document.querySelectorAll('.age-tab').forEach(t => t.classList.remove('active'));
                tab.classList.add('active');
                loadAgeCurriculum(ageKey);
            }
        });
    });

    // Mở cẩm nang phụ huynh
    const parentBtn = document.getElementById('parent-guide-btn');
    if (parentBtn) {
        parentBtn.addEventListener('click', () => {
            soundFx.playPop();
            openParentGuideModal();
        });
    }

    // Đóng các modal
    document.getElementById('close-studio-btn')?.addEventListener('click', closeVoiceStudio);
    document.getElementById('close-parent-modal')?.addEventListener('click', closeParentGuideModal);
    document.getElementById('resume-eyecare-btn')?.addEventListener('click', dismissEyeCareModal);

    // Nút Micro lớn trong phòng luyện nói
    const bigMicBtn = document.getElementById('big-mic-btn');
    if (bigMicBtn) {
        bigMicBtn.addEventListener('click', handleMicButtonClick);
    }
}

// ============================================================================
// API Calls & Data Loading
// ============================================================================
async function loadUserStats() {
    try {
        const res = await fetch('/api/stats');
        if (res.ok) {
            const data = await res.json();
            AppState.stats = data;
            updateStatsUI();
        }
    } catch (e) {
        console.warn('Lỗi tải thống kê:', e);
    }
}

function updateStatsUI() {
    const starCountEl = document.getElementById('user-stars-count');
    if (starCountEl) {
        starCountEl.textContent = AppState.stats.total_stars;
    }
}

async function loadAgeCurriculum(ageKey) {
    AppState.currentAge = ageKey;
    const contentArea = document.getElementById('main-dynamic-content');
    if (!contentArea) return;

    contentArea.innerHTML = `
        <div style="text-align: center; padding: 60px 20px;">
            <div style="font-size: 50px; animation: spin 1.5s infinite linear;">🌸</div>
            <p style="font-size: 18px; font-weight: 800; color: #636E72; margin-top: 14px;">Đang tải bài học vui nhộn cho bé...</p>
        </div>
    `;

    try {
        const res = await fetch(`/api/curriculum/${ageKey}`);
        if (res.ok) {
            const json = await res.json();
            AppState.curriculumData = json.data;
            renderAgeView(json.data);
        }
    } catch (err) {
        console.error('Lỗi nạp bài học:', err);
        contentArea.innerHTML = `<p style="text-align:center; padding:40px; color:#FF7675; font-weight:800;">Không thể tải bài học. Vui lòng thử lại.</p>`;
    }
}

// ============================================================================
// Render UI theo từng độ tuổi
// ============================================================================
function renderAgeView(data) {
    const contentArea = document.getElementById('main-dynamic-content');
    if (!contentArea) return;

    let html = `
        <div class="stage-banner">
            <div class="stage-text">
                <h2>${data.title} - ${data.stage}</h2>
                <p>${data.description}</p>
                <div class="stage-milestones">
                    ${data.milestones.map(m => `<span class="milestone-tag">✓ ${m}</span>`).join('')}
                </div>
            </div>
        </div>
    `;

    if (AppState.currentAge === 'age_2' || AppState.currentAge === 'age_3') {
        html += renderCategoriesCards(data.categories);
    } else if (AppState.currentAge === 'age_4') {
        html += renderAge4Garden(data);
    } else if (AppState.currentAge === 'age_5') {
        html += renderAge5Preschool(data);
    }

    contentArea.innerHTML = html;
    attachCardEvents();
}

// Render danh sách Flashcards (Cho bé 2 và 3 tuổi)
function renderCategoriesCards(categories) {
    if (!categories) return '';
    return categories.map(cat => `
        <div class="category-block">
            <div class="category-header">
                <span style="font-size: 28px;">${cat.icon}</span>
                <h3>${cat.name}</h3>
            </div>
            <div class="cards-grid">
                ${cat.items.map(item => `
                    <div class="kid-card" data-item='${JSON.stringify(item)}'>
                        <div class="kid-card-icon">${item.icon || '🌸'}</div>
                        <div class="kid-card-title">${item.word}</div>
                        <div class="kid-card-sound">${item.sound_text || item.word}</div>
                        <div class="kid-card-sentence">${item.sentence || ''}</div>
                        <div class="kid-card-actions">
                            <button class="card-btn speak-btn" onclick="event.stopPropagation(); playWordVoice('${item.word}')">
                                🔊 Nghe
                            </button>
                            <button class="card-btn record-btn" onclick="event.stopPropagation(); openVoiceStudio(${JSON.stringify(item).replace(/"/g, '&quot;')})">
                                🎤 Bé Nói
                            </button>
                        </div>
                    </div>
                `).join('')}
            </div>
        </div>
    `).join('');
}

// Render Khu vườn đồng dao & Kể chuyện (Lớp 4 tuổi)
function renderAge4Garden(data) {
    let html = `
        <div class="sub-nav-tabs">
            <button class="sub-nav-btn active" onclick="switchAge4Tab('rhymes')">📖 Khu Vườn Đồng Dao</button>
            <button class="sub-nav-btn" onclick="switchAge4Tab('stories')">🎨 Kể Chuyện Theo Tranh</button>
        </div>
        <div id="age4-tab-content">
            ${renderRhymesList(data.rhymes)}
        </div>
    `;
    return html;
}

function renderRhymesList(rhymes) {
    if (!rhymes) return '';
    return rhymes.map(r => `
        <div class="rhyme-card">
            <div class="rhyme-illustration">
                <div class="rhyme-icon">${r.icon}</div>
                <h4 style="font-weight:900; font-size:20px; color:#2D3436; margin-bottom:8px;">${r.title}</h4>
                <button class="header-btn" style="background:#FF4757; color:white; width:100%; justify-content:center;" onclick="playRhymeLyrics('${r.id}')">
                    ▶️ Đọc Vang Cùng Cô
                </button>
            </div>
            <div class="rhyme-content">
                <h3>${r.title}</h3>
                <p>${r.description}</p>
                <div class="rhyme-lyrics" id="lyrics-${r.id}">
                    ${r.lines.map((line, idx) => `<div class="rhyme-line" id="line-${r.id}-${idx}">${line}</div>`).join('')}
                </div>
            </div>
        </div>
    `).join('');
}

function renderStoriesList(stories) {
    if (!stories) return '';
    return stories.map(s => `
        <div class="rhyme-card" style="grid-template-columns: 1fr;">
            <div class="rhyme-content">
                <div style="display:flex; align-items:center; gap:12px; margin-bottom:12px;">
                    <span style="font-size:36px;">${s.icon}</span>
                    <div>
                        <h3>${s.title}</h3>
                        <p>${s.summary}</p>
                    </div>
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-top: 16px;">
                    ${s.scenes.map(sc => `
                        <div style="background:#F8F9FA; border-radius:18px; padding:18px; text-align:center; border:2px solid #DFE6E9; cursor:pointer;" onclick="playWordVoice('${sc.text}')">
                            <div style="font-size:50px; margin-bottom:8px;">${sc.image_icon}</div>
                            <div style="font-size:12px; font-weight:800; color:#FF4757; margin-bottom:6px;">Cảnh ${sc.step}</div>
                            <p style="font-size:14px; font-weight:700; color:#2D3436; line-height:1.4;">${sc.text}</p>
                            <div style="margin-top:8px; font-size:12px; color:#0984E3; font-weight:800;">❓ ${sc.prompt}</div>
                        </div>
                    `).join('')}
                </div>
            </div>
        </div>
    `).join('');
}

window.switchAge4Tab = function(tabName) {
    soundFx.playPop();
    document.querySelectorAll('.sub-nav-btn').forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');

    const container = document.getElementById('age4-tab-content');
    if (!container || !AppState.curriculumData) return;

    if (tabName === 'rhymes') {
        container.innerHTML = renderRhymesList(AppState.curriculumData.rhymes);
    } else {
        container.innerHTML = renderStoriesList(AppState.curriculumData.stories);
    }
};

// Render Lớp 5 tuổi: Bảng 29 chữ cái, 6 Thanh Điệu & Cỗ Xe Ghép Vần
function renderAge5Preschool(data) {
    return `
        <!-- 6 Thanh Điệu -->
        <div class="category-block">
            <div class="category-header">
                <span style="font-size: 28px;">🎢</span>
                <h3>6 Thanh Điệu Tiếng Việt Kỳ Diệu</h3>
            </div>
            <div class="tones-grid">
                ${data.tones.map(t => `
                    <div class="tone-card" style="border-left-color: ${t.color}" onclick="playToneSample('${t.id}', '${t.example}')">
                        <div class="tone-symbol" style="color: ${t.color}">${t.symbol}</div>
                        <h4>${t.name}</h4>
                        <div style="font-size:12px; color:#636E72; font-weight:700; margin-bottom:6px;">${t.motion}</div>
                        <div class="tone-example">${t.example}</div>
                    </div>
                `).join('')}
            </div>
        </div>

        <!-- Cỗ Xe Lửa Ghép Vần -->
        <div class="train-wrapper">
            <div class="train-title">🚂 Cỗ Xe Lửa Ghép Vần Kỳ Diệu</div>
            <p style="font-size:15px; font-weight:700; color:#636E72; margin-bottom:20px;">
                Bé chạm vào các toa tàu để ghép phụ âm, nguyên âm và dấu thanh thành tiếng trọn vẹn!
            </p>
            <div class="train-carts">
                <div class="cart-box" id="train-consonant">B</div>
                <div class="cart-plus">+</div>
                <div class="cart-box" id="train-vowel">A</div>
                <div class="cart-plus">=</div>
                <div class="cart-box result-box" id="train-result" onclick="playCurrentTrain()">BA</div>
            </div>
            <div style="display:flex; justify-content:center; gap:10px; flex-wrap:wrap;">
                <button class="header-btn" onclick="updateTrainSyllable('B', 'A', 'BA')">B + A = BA 👨</button>
                <button class="header-btn" onclick="updateTrainSyllable('B', 'A', 'BÀ')">B + A + ` = BÀ 👵</button>
                <button class="header-btn" onclick="updateTrainSyllable('C', 'A', 'CÁ')">C + A + ´ = CÁ 🐟</button>
                <button class="header-btn" onclick="updateTrainSyllable('M', 'E', 'MẸ')">M + E + . = MẸ 👩</button>
            </div>
        </div>

        <!-- Bảng 29 Chữ Cái Chuẩn Bộ GD&ĐT -->
        <div class="category-block">
            <div class="category-header">
                <span style="font-size: 28px;">🅰️</span>
                <h3>Bảng 29 Chữ Cái Tiếng Việt Chuẩn</h3>
            </div>
            <div class="alphabet-grid">
                ${data.alphabet.map(letter => `
                    <div class="letter-tile" onclick="playLetterSound('${letter.letter}', '${letter.sound}', '${letter.word}')">
                        <div class="letter-char">${letter.letter}</div>
                        <div style="font-size:22px;">${letter.icon}</div>
                        <div class="letter-word">${letter.word}</div>
                    </div>
                `).join('')}
            </div>
        </div>
    `;
}

// ============================================================================
// Tương tác âm thanh & Phát âm
// ============================================================================
function attachCardEvents() {
    // Đăng ký sự kiện chạm lật mở hoặc nghe
    document.querySelectorAll('.kid-card').forEach(card => {
        card.addEventListener('click', () => {
            const raw = card.dataset.item;
            if (raw) {
                const item = JSON.parse(raw);
                playWordVoice(item.word);
            }
        });
    });
}

function playWordVoice(text) {
    soundFx.playPop();
    speechEngine.speak(text);
}

function playLetterSound(letter, sound, word) {
    soundFx.playStar();
    speechEngine.speak(`Chữ ${letter}. Âm ${sound}. ${word}`);
}

function playToneSample(toneId, examples) {
    soundFx.playToneNote(toneId);
    setTimeout(() => {
        speechEngine.speak(examples);
    }, 400);
}

function updateTrainSyllable(c, v, res) {
    soundFx.playStar();
    document.getElementById('train-consonant').textContent = c;
    document.getElementById('train-vowel').textContent = v;
    const resBox = document.getElementById('train-result');
    resBox.textContent = res;
    speechEngine.speak(`${c}... ${v}... ${res}!`);
}

function playCurrentTrain() {
    const res = document.getElementById('train-result')?.textContent || 'BA';
    soundFx.playStar();
    speechEngine.speak(res);
}

function playRhymeLyrics(rhymeId) {
    const lyricsContainer = document.getElementById(`lyrics-${rhymeId}`);
    if (!lyricsContainer) return;

    soundFx.playStar();
    const lines = Array.from(lyricsContainer.querySelectorAll('.rhyme-line'));
    let currentIdx = 0;

    function readNextLine() {
        if (currentIdx >= lines.length) return;
        lines.forEach(l => l.classList.remove('active-line'));
        lines[currentIdx].classList.add('active-line');
        const text = lines[currentIdx].textContent;

        speechEngine.speak(text, () => {
            currentIdx++;
            setTimeout(readNextLine, 350);
        });
    }

    readNextLine();
}

// ============================================================================
// Voice Studio (Phòng luyện nói & nhận diện giọng bé)
// ============================================================================
function openVoiceStudio(item) {
    AppState.voiceStudioTarget = item;
    soundFx.playPop();

    const modal = document.getElementById('voice-studio-modal');
    if (!modal) return;

    document.getElementById('studio-icon').textContent = item.icon || '🌸';
    document.getElementById('studio-word').textContent = item.word;
    document.getElementById('studio-guide').textContent = item.mouth_guide || `Bé cùng cô nói to rõ ràng: "${item.word}" nhé!`;
    document.getElementById('speech-result-box').innerHTML = `
        <div style="font-size:15px; font-weight:800; color:#636E72;">
            Bấm chiếc Micro màu sắc bên dưới để bắt đầu nói nào!
        </div>
    `;

    modal.style.display = 'flex';

    // Đọc mẫu từ cho bé nghe ngay khi mở
    setTimeout(() => {
        speechEngine.speak(item.word);
    }, 400);
}

function closeVoiceStudio() {
    soundFx.playPop();
    speechEngine.stopListening();
    speechEngine.stopSpeaking();
    const modal = document.getElementById('voice-studio-modal');
    if (modal) modal.style.display = 'none';
}

function handleMicButtonClick() {
    const micBtn = document.getElementById('big-mic-btn');
    const hint = document.getElementById('mic-hint-text');
    const target = AppState.voiceStudioTarget;
    if (!target) return;

    soundFx.playPop();
    micBtn.classList.add('listening');
    hint.textContent = "Đang lắng nghe bé nói...";

    const ok = speechEngine.startListening(async (transcript, error) => {
        micBtn.classList.remove('listening');

        if (error) {
            hint.textContent = "Không nghe rõ. Bé bấm mic thử lại nhé!";
            return;
        }

        hint.textContent = `Bé vừa nói: "${transcript || '...'}"`;
        await evaluateBabySpeech(target.word, transcript);
    });

    if (!ok) {
        micBtn.classList.remove('listening');
        hint.textContent = "Chưa kết nối được Micro.";
    }
}

async function evaluateBabySpeech(targetText, spokenText) {
    const resultBox = document.getElementById('speech-result-box');
    resultBox.innerHTML = `<div style="font-weight:800; color:#0984E3;">Cô giáo đang lắng nghe và chấm điểm...</div>`;

    try {
        const res = await fetch('/api/speech/evaluate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                target_text: targetText,
                spoken_text: spokenText || targetText,
                age_group: AppState.currentAge
            })
        });

        if (res.ok) {
            const result = await res.json();

            // Hiệu ứng ăn mừng
            if (result.stars >= 3) {
                soundFx.playCheer();
            } else {
                soundFx.playStar();
            }

            const starsHtml = '⭐'.repeat(result.stars);

            resultBox.innerHTML = `
                <div class="stars-celebration">${starsHtml}</div>
                <div class="speech-feedback-text">${result.feedback}</div>
                <div style="font-size:13px; font-weight:700; color:#636E72; margin-top:6px;">
                    Điểm số: ${result.score}/100 • Bé nói: "${result.spoken_text || targetText}"
                </div>
            `;

            // Đọc lời động viên
            setTimeout(() => {
                speechEngine.speak(result.encouragement_audio);
            }, 600);

            // Cập nhật số sao
            AppState.stats.total_stars += result.stars;
            updateStatsUI();

            // Ghi nhận vào bài học
            await recordItemLearned(AppState.voiceStudioTarget.id, result.stars);
        }
    } catch (e) {
        console.error('Lỗi chấm điểm giọng nói:', e);
    }
}

async function recordItemLearned(itemId, stars) {
    try {
        await fetch('/api/practice/record', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                item_id: itemId,
                age_group: AppState.currentAge,
                stars_earned: stars,
                duration_seconds: 30
            })
        });
    } catch (e) {
        // silent
    }
}

// ============================================================================
// Cẩm Nang Phụ Huynh Modal
// ============================================================================
async function openParentGuideModal() {
    const modal = document.getElementById('parent-modal');
    if (!modal) return;

    modal.style.display = 'flex';
    const listContainer = document.getElementById('parent-guide-list');
    listContainer.innerHTML = '<p style="text-align:center;">Đang tải cẩm nang chuyên gia...</p>';

    try {
        const res = await fetch('/api/parenting-guide');
        if (res.ok) {
            const data = await res.json();
            listContainer.innerHTML = data.guides.map(g => `
                <div class="guide-item-card" style="border-left-color: ${g.color || '#1E90FF'}">
                    <h4>${g.icon} ${g.title} (${g.category})</h4>
                    <p style="font-size:14px; font-weight:700; color:#2D3436; margin-bottom:10px;">${g.summary}</p>
                    <ul>
                        ${g.content.map(c => `<li>${c}</li>`).join('')}
                    </ul>
                </div>
            `).join('');
        }
    } catch (e) {
        listContainer.innerHTML = '<p style="color:red;">Không thể tải dữ liệu.</p>';
    }
}

function closeParentGuideModal() {
    soundFx.playPop();
    const modal = document.getElementById('parent-modal');
    if (modal) modal.style.display = 'none';
}

// ============================================================================
// Bảo Vệ Mắt Cho Bé (Eye-Care Timer)
// ============================================================================
function startEyeCareTimer() {
    AppState.eyeCareTimerId = setInterval(() => {
        AppState.eyeCareSeconds++;
        if (AppState.eyeCareSeconds >= AppState.eyeCareMaxSeconds) {
            showEyeCareModal();
            AppState.eyeCareSeconds = 0;
        }
    }, 1000);
}

function showEyeCareModal() {
    const modal = document.getElementById('eyecare-modal');
    if (modal) {
        soundFx.playCheer();
        modal.style.display = 'flex';
        speechEngine.speak("Bé ơi, mình đã học tập rất chăm chỉ rồi! Cùng nghỉ mắt và tập thể dục một chút nhé!");
    }
}

function dismissEyeCareModal() {
    soundFx.playPop();
    const modal = document.getElementById('eyecare-modal');
    if (modal) modal.style.display = 'none';
    AppState.eyeCareSeconds = 0;
}
