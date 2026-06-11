---
title: QR Elite Designer
emoji: 🎯
colorFrom: indigo
colorTo: gray
sdk: static
app_file: index.html
pinned: false
---

# QR Elite | Professional QR Identity Designer

[![Python CI](https://github.com/ShreyData/QR_generator/actions/workflows/test.yml/badge.svg)](https://github.com/ShreyData/QR_generator/actions/workflows/test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**QR Elite** is a high-performance, aesthetically driven QR code generator. Built for designers and developers, it transforms standard scannable data into a unique digital identity with professional themes, custom branding, and modern module shapes.

## ✨ Key Features

- **Professional Presets:** 15+ curated themes including *Snapchat*, *Cyberpunk*, *Royal Gold*, and *Minimal Dot*.
- **Custom Branding:** Seamlessly embed brand logos with high error correction (ECC).
- **Modern Module Shapes:** Advanced architecture including *Modern Dots*, *Liquid Rounded*, and *Linear Bar* styles.
- **Decoupled Architecture:** Stateless Flask API (Backend) + Tailwind CSS SPA (Frontend).
- **HD Export:** High-definition assets optimized for both digital and print.

## 🛠 Tech Stack

- **Backend:** Python, Flask, `qrcode`, Pillow, Gunicorn.
- **Frontend:** Vanilla JS (SPA), Tailwind CSS, FontAwesome.
- **CI/CD:** GitHub Actions.

## 🚀 Quick Start

### Local Development

1. **Clone & Setup Backend:**
   ```bash
   pip install -r requirements.txt
   python app.py
   ```
   The API will start at `http://127.0.0.1:5000/api/generate`.

2. **Launch Frontend:**
   Open `frontend/index.html` in your browser. The UI is pre-configured to connect to your local backend terminal.

## 🤝 Contributing

We welcome contributions! Whether it's adding new themes, improving the UI, or optimizing the QR engine, please check out our [Contributing Guidelines](CONTRIBUTING.md).

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
