# QR Elite | Professional QR Designer

[![Python CI](https://github.com/ShreyData/QR_generator/actions/workflows/test.yml/badge.svg)](https://github.com/ShreyData/QR_generator/actions/workflows/test.yml)

**QR Elite** is a high-performance, aesthetically driven QR code generator. Built for designers and developers, it transforms standard scannable data into a unique digital identity with professional themes, custom branding, and modern module shapes.

## ✨ Key Features

- **Professional Presets:** Choose from 15+ curated themes including *Snapchat*, *Cyberpunk*, *Royal Gold*, and *Minimal Dot*.
- **Custom Branding:** Seamlessly embed brand logos with high error correction (ECC) for guaranteed scannability.
- **Modern Module Shapes:** Go beyond squares with *Modern Dots*, *Liquid Rounded*, and *Bar* styles.
- **Decoupled Architecture:** Stateless Flask API (Backend) + Tailwind CSS SPA (Frontend).
- **HD Export:** High-definition PNG assets suitable for print and digital use.

## 🛠 Tech Stack

- **Backend:** Python, Flask, `qrcode`, Pillow, Gunicorn.
- **Frontend:** Vanilla JS, Tailwind CSS, FontAwesome.
- **Infrastructure:** GitHub Actions (CI/CD), Render (API), Hugging Face (Static Hosting).

## 🚀 Quick Start

### Local Development

1. **Clone & Setup Backend:**
   ```bash
   pip install -r requirements.txt
   python app.py
   ```
   The API will start at `http://127.0.0.1:5000/api/generate`.

2. **Launch Frontend:**
   Simply open `frontend/index.html` in your browser. The UI is pre-configured to connect to your local backend.

## 📖 Documentation

- [Deployment Guide](docs/deploy.md) - Detailed steps for Render & Hugging Face.
- [API Reference](qr_app/routes.py) - Overview of the REST endpoints.

## 📄 License

This project is open-source and free to use. See individual files for specific logic.
