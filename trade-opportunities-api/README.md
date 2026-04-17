# 🇮🇳 Trade Opportunities API

A FastAPI service that gathers live market data and uses **Google Gemini AI** to generate structured Markdown trade-opportunity reports for Indian sectors.

---

## ✅ Features

| Feature | Detail |
|---|---|
| AI Analysis | Google Gemini 1.5 Flash (free tier) |
| Data Collection | DuckDuckGo search (no API key needed) |
| Authentication | JWT guest tokens (POST /auth/token) |
| Rate Limiting | 10 requests / 60 s per token (in-memory) |
| Session Tracking | In-memory session log |
| Output Format | Markdown report |

---

## 🛠️ Setup (Step-by-Step for VS Code Beginners)

### Step 1 – Install Python
Download Python 3.11+ from https://www.python.org/downloads/  
During install, **tick "Add Python to PATH"**.

### Step 2 – Open the project in VS Code
1. Open VS Code
2. File → Open Folder → select the `trade-opportunities-api` folder

### Step 3 – Open the terminal in VS Code
Press `` Ctrl+` `` (backtick) or go to **Terminal → New Terminal**

### Step 4 – Create a virtual environment
```bash
python -m venv venv
```

### Step 5 – Activate the virtual environment
**Windows:**
```bash
venv\Scripts\activate
```
**Mac/Linux:**
```bash
source venv/bin/activate
```
You should now see `(venv)` at the start of your terminal line.

### Step 6 – Install dependencies
```bash
pip install -r requirements.txt
```

### Step 7 – Get a FREE Gemini API key
1. Go to https://aistudio.google.com/app/apikey
2. Sign in with a Google account
3. Click **"Create API key"**
4. Copy the key

### Step 8 – Create your `.env` file
1. Copy `.env.example` to a new file called `.env`
2. Paste your Gemini key:
```
GEMINI_API_KEY=AIza...your_key_here
SECRET_KEY=any-random-secret-string-123
```

### Step 9 – Run the server
```bash
uvicorn main:app --reload
```

You'll see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

---

## 🚀 How to Use the API

Open your browser and go to:  
👉 **http://127.0.0.1:8000/docs**

This opens the interactive Swagger UI where you can test everything!

### Option A – Use Swagger UI (easiest)
1. Go to `http://127.0.0.1:8000/docs`
2. Click **POST /auth/token** → **Try it out** → **Execute**
3. Copy the `access_token` value from the response
4. Click **GET /analyze/{sector}** → **Try it out**
5. Enter the token in the `authorization` field as: `Bearer <your_token>`
6. Enter a sector name (e.g. `pharmaceuticals`)
7. Click **Execute** – you'll get a Markdown report!

### Option B – Use curl (command line)
```bash
# Step 1: Get a token
curl -X POST http://127.0.0.1:8000/auth/token

# Step 2: Use the token to analyze a sector
curl -X GET http://127.0.0.1:8000/analyze/pharmaceuticals \
  -H "authorization: Bearer <paste_token_here>"
```

### Save the report to a file
```bash
curl -X GET http://127.0.0.1:8000/analyze/technology \
  -H "authorization: Bearer <token>" \
  -o technology_report.md
```

---

## 📋 Supported Sectors

```
pharmaceuticals  |  technology   |  agriculture  |  textiles
automobiles      |  finance      |  energy       |  infrastructure
chemicals        |  fmcg         |  defence      |  retail
```

---

## 🔗 All Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/auth/token` | Get a guest JWT token |
| GET | `/analyze/{sector}` | Get trade analysis report |
| GET | `/rate-limit-status` | Check remaining requests |
| GET | `/sessions` | View session stats |
| GET | `/docs` | Swagger UI (interactive docs) |

---

## 📁 Project Structure

```
trade-opportunities-api/
├── main.py             ← FastAPI app + all routes
├── config.py           ← Settings (reads .env)
├── auth.py             ← JWT token creation & verification
├── rate_limiter.py     ← In-memory sliding window rate limiter
├── data_collector.py   ← DuckDuckGo search scraper
├── ai_analyzer.py      ← Google Gemini AI integration
├── session_manager.py  ← In-memory session tracking
├── requirements.txt    ← Python packages
├── .env.example        ← Template for your .env file
└── README.md           ← This file
```

---

## ❓ Troubleshooting

**"ModuleNotFoundError"** → Run `pip install -r requirements.txt`  
**"GEMINI_API_KEY not set"** → Make sure your `.env` file exists and has the key  
**401 Unauthorized** → POST to `/auth/token` first and use `Bearer <token>`  
**429 Too Many Requests** → Wait 60 seconds, then try again  
**Port already in use** → Run `uvicorn main:app --reload --port 8001`

---

*Built with FastAPI + Google Gemini + DuckDuckGo Search*
