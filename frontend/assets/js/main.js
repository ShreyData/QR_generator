/**
 * QR Elite - Professional Logic Controller
 */

const App = {
    state: {
        logo: null,
        currentTheme: null,
        isGenerating: false,
        apiUrl: window.location.hostname.includes('localhost') || window.location.hostname.includes('127.0.0.1')
               ? 'http://127.0.0.1:5000/api/generate'
               : 'https://YOUR-RENDER-BACKEND.onrender.com/api/generate'
    },

    themes: [
        { id: 'classic', name: 'Elite Dark', fill: '#0f172a', back: '#ffffff', shape: 'square', icon: 'square' },
        { id: 'snap', name: 'Snap Style', fill: '#000000', back: '#FFFC00', shape: 'circle', icon: 'ghost' },
        { id: 'neon', name: 'Cyber Neon', fill: '#38bdf8', back: '#020617', shape: 'gapped', icon: 'bolt' },
        { id: 'royal', name: 'Royal Gold', fill: '#854d0e', back: '#fffbeb', shape: 'rounded', icon: 'crown' },
        { id: 'forest', name: 'Eco Forest', fill: '#064e3b', back: '#f0fdf4', shape: 'rounded', icon: 'leaf' },
        { id: 'minimal', name: 'Pure Minimal', fill: '#64748b', back: '#ffffff', shape: 'circle', icon: 'ellipsis' },
        { id: 'bars', name: 'Modern Bars', fill: '#1e1b4b', back: '#ffffff', shape: 'vertical', icon: 'align-center' },
        { id: 'dino', name: 'Pixel Dino', fill: '#166534', back: '#f8fafc', shape: 'gapped', icon: 'gamepad' },
        { id: 'berry', name: 'Berry Red', fill: '#991b1b', back: '#fff1f2', shape: 'rounded', icon: 'heart' }
    ],

    init() {
        this.cacheDOM();
        this.renderThemes();
        this.bindEvents();
        console.log("QR Elite Engine Initialized...");
    },

    cacheDOM() {
        this.dom = {
            dataInput: document.getElementById('qr-data'),
            fillInput: document.getElementById('qr-fill'),
            backInput: document.getElementById('qr-back'),
            shapeInput: document.getElementById('qr-shape'),
            logoInput: document.getElementById('qr-logo'),
            logoLabel: document.getElementById('logo-label'),
            generateBtn: document.getElementById('generate-btn'),
            previewImg: document.getElementById('qr-preview'),
            resultBox: document.getElementById('qr-result-container'),
            placeholder: document.getElementById('preview-placeholder'),
            downloadBtn: document.getElementById('download-btn'),
            loader: document.getElementById('loading-overlay'),
            themeGallery: document.getElementById('theme-gallery'),
            resetBtn: document.getElementById('reset-btn')
        };
    },

    renderThemes() {
        this.dom.themeGallery.innerHTML = this.themes.map((t, i) => `
            <div class="theme-card p-3 rounded-xl border border-slate-200 bg-white cursor-pointer group shadow-sm hover:shadow-md transition-all ${i === 0 ? 'active border-blue-500 ring-2 ring-blue-50' : ''}" 
                 data-theme-id="${t.id}">
                <div class="w-full aspect-square rounded-lg mb-2 flex items-center justify-center" style="background: ${t.back}">
                    <i class="fas fa-${t.icon} text-lg" style="color: ${t.fill}"></i>
                </div>
                <p class="text-[9px] font-bold uppercase tracking-tighter text-slate-500 group-hover:text-slate-900 text-center">${t.name}</p>
            </div>
        `).join('');
    },

    bindEvents() {
        // Theme Selection
        this.dom.themeGallery.addEventListener('click', (e) => {
            const card = e.target.closest('.theme-card');
            if (!card) return;
            
            const theme = this.themes.find(t => t.id === card.dataset.themeId);
            this.applyTheme(theme, card);
        });

        // Logo Upload
        this.dom.logoInput.addEventListener('change', (e) => {
            const file = e.target.files[0];
            if (file) {
                this.dom.logoLabel.innerHTML = `<i class="fas fa-check-circle text-green-500 mr-2"></i> ${file.name}`;
                const reader = new FileReader();
                reader.onload = (ev) => this.state.logo = ev.target.result;
                reader.readAsDataURL(file);
            }
        });

        // Generate Action
        this.dom.generateBtn.onclick = () => this.generate();
        
        // Download Action
        this.dom.downloadBtn.onclick = () => this.download();

        // Reset Action
        this.dom.resetBtn.onclick = () => this.reset();
    },

    applyTheme(theme, card) {
        // Update UI
        document.querySelectorAll('.theme-card').forEach(c => c.classList.remove('active', 'border-blue-500', 'ring-2', 'ring-blue-50'));
        card.classList.add('active', 'border-blue-500', 'ring-2', 'ring-blue-50');

        // Update Inputs
        this.dom.fillInput.value = theme.fill;
        this.dom.backInput.value = theme.back;
        this.dom.shapeInput.value = theme.shape;
    },

    async generate() {
        const text = this.dom.dataInput.value.trim();
        if (!text) {
            this.shake(this.dom.dataInput);
            return;
        }

        this.setLoading(true);

        try {
            const response = await fetch(this.state.apiUrl, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    qr_data: text,
                    fill_color: this.dom.fillInput.value,
                    back_color: this.dom.backInput.value,
                    shape: this.dom.shapeInput.value,
                    logo: this.state.logo
                })
            });

            const data = await response.json();
            if (data.success) {
                this.showResult(data.image);
            } else {
                alert("Error: " + data.error);
            }
        } catch (err) {
            console.error(err);
            alert("Connection Failed. Is the backend running?");
        } finally {
            this.setLoading(false);
        }
    },

    showResult(base64) {
        this.dom.placeholder.classList.add('hidden');
        this.dom.resultBox.classList.remove('hidden');
        this.dom.previewImg.src = base64;
        this.dom.downloadBtn.disabled = false;
        
        // Animate result
        this.dom.previewImg.classList.add('animate-in');
        setTimeout(() => this.dom.previewImg.classList.remove('animate-in'), 600);
    },

    setLoading(isLoading) {
        this.state.isGenerating = isLoading;
        this.dom.loader.classList.toggle('hidden', !isLoading);
        this.dom.generateBtn.disabled = isLoading;
        this.dom.generateBtn.innerHTML = isLoading 
            ? '<i class="fas fa-spinner fa-spin mr-2"></i> Finalizing Design...' 
            : 'Generate HD Asset';
    },

    download() {
        const link = document.createElement('a');
        link.href = this.dom.previewImg.src;
        link.download = `QR_Elite_${Date.now()}.png`;
        link.click();
    },

    reset() {
        this.dom.dataInput.value = '';
        this.dom.placeholder.classList.remove('hidden');
        this.dom.resultBox.classList.add('hidden');
        this.dom.downloadBtn.disabled = true;
        this.state.logo = null;
        this.dom.logoLabel.innerText = 'Upload Brand Logo';
        this.dom.logoInput.value = '';
    },

    shake(el) {
        el.classList.add('ring-2', 'ring-red-400');
        setTimeout(() => el.classList.remove('ring-2', 'ring-red-400'), 1000);
        el.focus();
    }
};

document.addEventListener('DOMContentLoaded', () => App.init());
