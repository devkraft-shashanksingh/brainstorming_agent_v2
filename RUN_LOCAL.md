# Local Development Guide

Follow these steps to run the Brainstorming Agent on your local machine.

## Prerequisites
*   Python 3.10+
*   Node.js 18+ & npm
*   Google Gemini API Key

---

## 1. Backend Setup (Python)

All backend code is now located in the `backend/` directory.

1.  **Navigate to Backend**:
    ```bash
    cd backend
    ```
2.  **Create Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure Environment**:
    Ensure the `.env` file exists in the `backend/` folder and contains your `GEMINI_API_KEY`.
5.  **Run Backend**:
    ```bash
    uvicorn data_library.api:app --reload --port 8000
    ```
    The backend will be available at `http://localhost:8000`.

---

## 2. Frontend Setup (Next.js)

All frontend code is now located in the `frontend/` directory.

1.  **Navigate to Frontend**:
    ```bash
    cd frontend
    ```
2.  **Install Dependencies**:
    ```bash
    npm install
    ```
3.  **Run Frontend**:
    ```bash
    npm run dev
    ```
    The frontend will be available at `http://localhost:3000`.

---

## 3. Verification
1.  Open `http://localhost:3000` in your browser.
2.  Enter a brief and click "Generate".
3.  The frontend will call the backend at `http://localhost:8000`.
