/**
 * speech_engine.js - Bộ xử lý giọng nói Tiếng Việt (TTS & STT)
 * Tối ưu hóa đặc thù cho việc dạy trẻ mầm non học nói.
 */

class SpeechEngine {
    constructor() {
        this.synth = window.speechSynthesis;
        this.voices = [];
        this.selectedVoice = null;
        this.rate = 0.85; // Tốc độ đọc chậm rãi, rõ ràng cho bé nghe
        this.pitch = 1.15; // Giọng hơi cao vui tươi, ấm áp như cô giáo mầm non
        this.isSpeaking = false;

        // Khởi tạo nhận diện giọng nói (STT)
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        this.recognition = SpeechRecognition ? new SpeechRecognition() : null;
        this.isListening = false;
        this.currentListenerCallback = null;

        this.initVoices();
        this.initRecognition();
    }

    initVoices() {
        if (!this.synth) return;

        const updateVoices = () => {
            this.voices = this.synth.getVoices();
            // Ưu tiên giọng tiếng Việt
            const viVoices = this.voices.filter(v => v.lang.includes('vi') || v.lang.includes('VI'));
            if (viVoices.length > 0) {
                // Ưu tiên giọng nữ truyền cảm hoặc HoaiMy / Google Tiếng Việt
                const femaleVi = viVoices.find(v => v.name.includes('HoaiMy') || v.name.includes('Google') || v.name.includes('Female'));
                this.selectedVoice = femaleVi || viVoices[0];
            } else if (this.voices.length > 0) {
                this.selectedVoice = this.voices[0];
            }
        };

        updateVoices();
        if (this.synth.onvoiceschanged !== undefined) {
            this.synth.onvoiceschanged = updateVoices;
        }
    }

    initRecognition() {
        if (!this.recognition) return;

        this.recognition.lang = 'vi-VN';
        this.recognition.continuous = false;
        this.recognition.interimResults = false;
        this.recognition.maxAlternatives = 3;

        this.recognition.onstart = () => {
            this.isListening = true;
            if (this.onListenStateChange) this.onListenStateChange(true);
        };

        this.recognition.onresult = (event) => {
            let bestTranscript = "";
            if (event.results && event.results.length > 0) {
                bestTranscript = event.results[0][0].transcript;
            }
            if (this.currentListenerCallback) {
                this.currentListenerCallback(bestTranscript, null);
            }
        };

        this.recognition.onerror = (event) => {
            console.warn("Lỗi nhận diện âm thanh:", event.error);
            if (this.currentListenerCallback) {
                this.currentListenerCallback("", event.error);
            }
        };

        this.recognition.onend = () => {
            this.isListening = false;
            if (this.onListenStateChange) this.onListenStateChange(false);
        };
    }

    speak(text, onEndCallback = null) {
        if (!this.synth) return;

        // Dừng câu đang đọc dở nếu có
        this.synth.cancel();

        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = 'vi-VN';
        utterance.rate = this.rate;
        utterance.pitch = this.pitch;

        if (this.selectedVoice) {
            utterance.voice = this.selectedVoice;
        }

        utterance.onstart = () => {
            this.isSpeaking = true;
            if (this.onSpeakStateChange) this.onSpeakStateChange(true, text);
        };

        utterance.onend = () => {
            this.isSpeaking = false;
            if (this.onSpeakStateChange) this.onSpeakStateChange(false, text);
            if (onEndCallback) onEndCallback();
        };

        utterance.onerror = () => {
            this.isSpeaking = false;
            if (this.onSpeakStateChange) this.onSpeakStateChange(false, text);
            if (onEndCallback) onEndCallback();
        };

        this.synth.speak(utterance);
    }

    stopSpeaking() {
        if (this.synth) {
            this.synth.cancel();
            this.isSpeaking = false;
        }
    }

    startListening(callback) {
        if (!this.recognition) {
            alert("Trình duyệt hoặc hệ điều hành chưa hỗ trợ Micro nhận diện giọng nói Web Speech. Bé vẫn có thể nghe và bấm nút để tập nói nhé!");
            return false;
        }

        // Dừng đọc trước khi nghe
        this.stopSpeaking();

        this.currentListenerCallback = callback;
        try {
            this.recognition.start();
            return true;
        } catch (e) {
            console.warn("Lỗi khởi động nhận diện:", e);
            try {
                this.recognition.stop();
                setTimeout(() => this.recognition.start(), 200);
                return true;
            } catch (err) {
                return false;
            }
        }
    }

    stopListening() {
        if (this.recognition && this.isListening) {
            this.recognition.stop();
            this.isListening = false;
        }
    }
}

window.speechEngine = new SpeechEngine();
