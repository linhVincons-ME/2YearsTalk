/**
 * audio_effects.js - Bộ tạo hiệu ứng âm thanh tổng hợp bằng Web Audio API
 * Hoạt động 100% Offline, không phụ thuộc file âm thanh ngoài.
 */
class SoundEffects {
    constructor() {
        this.ctx = null;
        this.enabled = true;
    }

    init() {
        if (!this.ctx) {
            const AudioContext = window.AudioContext || window.webkitAudioContext;
            if (AudioContext) {
                this.ctx = new AudioContext();
            }
        }
        if (this.ctx && this.ctx.state === 'suspended') {
            this.ctx.resume();
        }
    }

    playPop() {
        if (!this.enabled) return;
        this.init();
        if (!this.ctx) return;

        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        const now = this.ctx.currentTime;

        osc.type = 'sine';
        osc.frequency.setValueAtTime(400, now);
        osc.frequency.exponentialRampToValueAtTime(800, now + 0.08);

        gain.gain.setValueAtTime(0.3, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.08);

        osc.connect(gain);
        gain.connect(this.ctx.destination);

        osc.start(now);
        osc.stop(now + 0.08);
    }

    playStar() {
        if (!this.enabled) return;
        this.init();
        if (!this.ctx) return;

        const now = this.ctx.currentTime;
        const freqs = [523.25, 659.25, 783.99, 1046.50]; // C5, E5, G5, C6

        freqs.forEach((freq, index) => {
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            const noteTime = now + index * 0.07;

            osc.type = 'triangle';
            osc.frequency.setValueAtTime(freq, noteTime);

            gain.gain.setValueAtTime(0.2, noteTime);
            gain.gain.exponentialRampToValueAtTime(0.01, noteTime + 0.25);

            osc.connect(gain);
            gain.connect(this.ctx.destination);

            osc.start(noteTime);
            osc.stop(noteTime + 0.25);
        });
    }

    playCheer() {
        if (!this.enabled) return;
        this.init();
        if (!this.ctx) return;

        const now = this.ctx.currentTime;
        // Chuỗi hợp âm vinh quang
        const chord1 = [523.25, 659.25, 783.99]; // C
        const chord2 = [587.33, 739.99, 880.00]; // D
        const chord3 = [1046.50, 1318.51, 1567.98]; // C cao

        const playChord = (notes, time, duration) => {
            notes.forEach(f => {
                const osc = this.ctx.createOscillator();
                const gain = this.ctx.createGain();
                osc.type = 'sine';
                osc.frequency.setValueAtTime(f, time);
                gain.gain.setValueAtTime(0.15, time);
                gain.gain.exponentialRampToValueAtTime(0.001, time + duration);
                osc.connect(gain);
                gain.connect(this.ctx.destination);
                osc.start(time);
                osc.stop(time + duration);
            });
        };

        playChord(chord1, now, 0.2);
        playChord(chord2, now + 0.18, 0.2);
        playChord(chord3, now + 0.36, 0.6);
    }

    playToneNote(toneType) {
        if (!this.enabled) return;
        this.init();
        if (!this.ctx) return;

        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();

        osc.type = 'sine';
        gain.gain.setValueAtTime(0.25, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.5);

        if (toneType === 'tone_sac') {
            // Thanh sắc: trượt cao lên
            osc.frequency.setValueAtTime(440, now);
            osc.frequency.exponentialRampToValueAtTime(700, now + 0.35);
        } else if (toneType === 'tone_huyen') {
            // Thanh huyền: trượt trầm xuống
            osc.frequency.setValueAtTime(500, now);
            osc.frequency.exponentialRampToValueAtTime(320, now + 0.4);
        } else if (toneType === 'tone_hoi') {
            // Thanh hỏi: vòng lượn xuống rồi nhấc lên
            osc.frequency.setValueAtTime(450, now);
            osc.frequency.exponentialRampToValueAtTime(350, now + 0.2);
            osc.frequency.exponentialRampToValueAtTime(480, now + 0.45);
        } else if (toneType === 'tone_nga') {
            // Thanh ngã: nhấp nhô ngắt giọng
            osc.frequency.setValueAtTime(460, now);
            osc.frequency.exponentialRampToValueAtTime(600, now + 0.15);
            gain.gain.setValueAtTime(0.05, now + 0.18);
            gain.gain.setValueAtTime(0.25, now + 0.22);
            osc.frequency.setValueAtTime(620, now + 0.22);
            osc.frequency.exponentialRampToValueAtTime(650, now + 0.45);
        } else if (toneType === 'tone_nang') {
            // Thanh nặng: rơi dứt khoát
            osc.frequency.setValueAtTime(450, now);
            osc.frequency.exponentialRampToValueAtTime(220, now + 0.15);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.2);
        } else {
            // Thanh ngang: ngân êm dịu phẳng lặng
            osc.frequency.setValueAtTime(440, now);
        }

        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now);
        osc.stop(now + 0.5);
    }
}

window.soundFx = new SoundEffects();
