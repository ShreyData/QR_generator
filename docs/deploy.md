# Deployment Guide

This guide provides step-by-step instructions to deploy the **QR Elite** application. Because the project uses a decoupled architecture, the backend and frontend are hosted separately for maximum performance and scalability.

---

## 1. Backend Deployment (Render)

The backend is a Flask REST API. We use [Render](https://render.com/) for its excellent Python support and automatic SSL.

### Steps:
1.  **Create a Render Account:** Sign up at [render.com](https://render.com/).
2.  **New Web Service:** Click "New +" and select "Web Service".
3.  **Connect GitHub:** Link your GitHub account and select this repository.
4.  **Configure Environment:**
    *   **Runtime:** `Python 3`
    *   **Build Command:** `pip install -r requirements.txt`
    *   **Start Command:** `gunicorn "app:create_app()"`
5.  **Environment Variables (Optional):** Add any custom configs from `config.py` if needed.
6.  **Deploy:** Click "Create Web Service".
7.  **Note the URL:** Once deployed, Render will provide a URL (e.g., `https://qr-backend.onrender.com`). **Copy this URL.**

---

## 2. Frontend Deployment (Hugging Face Spaces)

The frontend is a static web application. [Hugging Face Spaces](https://huggingface.co/spaces) provides a free and fast way to host static content.

### Steps:
1.  **Update API URL:**
    *   Open `frontend/index.html` in your code editor.
    *   Find the `API_URL` variable in the `<script>` section (around line 200).
    *   Replace the placeholder with your **live Render URL** (e.g., `https://qr-backend.onrender.com/api/generate`).
2.  **Create a New Space:**
    *   Go to [huggingface.co/new-space](https://huggingface.co/new-space).
    *   Name your space (e.g., `elite-qr-generator`).
    *   **SDK:** Select **Static**.
    *   **Visibility:** Public.
3.  **Upload Files:**
    *   Upload the contents of the `frontend/` directory (not the directory itself, just the files inside).
    *   Alternatively, connect your GitHub repo and point the "Base directory" to `frontend`.
4.  **View Site:** Your professional QR generator is now live at `https://huggingface.co/spaces/YOUR_USER/YOUR_SPACE_NAME`.

---

## 3. CI/CD Integration

Every time you push code to the `main` branch:
*   **GitHub Actions** will run the test suite defined in `.github/workflows/test.yml`.
*   **Render** will automatically pull the changes and redeploy the backend.
*   **Hugging Face** (if linked to GitHub) will automatically update the frontend.
