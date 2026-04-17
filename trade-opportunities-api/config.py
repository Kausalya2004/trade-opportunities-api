"""
config.py – Central configuration (reads from .env automatically).
"""

import os
from dotenv import load_dotenv

load_dotenv()   # reads .env file if present


class Settings:
    # ── Gemini ───────────────────────────────────────────────────────────────
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    GEMINI_MODEL:   str = "gemini-1.5-flash"           # free-tier model

    # ── JWT / Auth ────────────────────────────────────────────────────────────
    SECRET_KEY:     str = os.getenv("SECRET_KEY", "change-this-secret-in-production")
    TOKEN_TTL_MINS: int = int(os.getenv("TOKEN_TTL_MINS", "60"))

    # ── Rate limiting ─────────────────────────────────────────────────────────
    RATE_LIMIT_REQUESTS: int = int(os.getenv("RATE_LIMIT_REQUESTS", "10"))
    RATE_LIMIT_WINDOW:   int = int(os.getenv("RATE_LIMIT_WINDOW", "60"))   # seconds


settings = Settings()
