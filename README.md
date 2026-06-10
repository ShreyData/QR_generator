# Professional QR Code Generator

A high-performance, customizable QR code generator with a decoupled architecture. 

## Features
- **Advanced Customization:**
  - Shapes: Standard, Dots, Rounded, Gapped.
  - Colors: Custom foreground and background colors.
  - Branding: Embed custom logos in the center of QR codes.
- **Modern UI:** Built with Tailwind CSS, fully responsive.
- **REST API:** Stateless backend ready for cloud deployment.
- **CI/CD:** Automated testing via GitHub Actions.

## Project Structure
- `qr_app/`: Flask backend logic and QR engine.
- `frontend/`: Standalone static frontend (HTML/JS).
- `.github/workflows/`: CI/CD pipelines.

## Local Development

### Backend
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the server:
   ```bash
   python app.py
   ```
   The API will be available at `http://127.0.0.1:5000/api/generate`.

### Frontend
Open `frontend/index.html` in any web browser.

## Deployment

### Backend (Render)
1. Create a new **Web Service** on [Render](https://render.com/).
2. Connect your GitHub repository.
3. Select **Python** as the runtime.
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `gunicorn "app:create_app()"`
6. Copy your Render URL and update the `API_URL` in `frontend/index.html`.

### Frontend (Hugging Face Pages / Spaces)
1. Create a new **Space** on [Hugging Face](https://huggingface.co/new-space).
2. Choose **Static** as the Space SDK.
3. Upload the contents of the `frontend/` directory (or connect your GitHub repo and configure the directory).

## CI/CD
The project includes a GitHub Action in `.github/workflows/test.yml` that automatically tests the QR engine on every push to `main`.
