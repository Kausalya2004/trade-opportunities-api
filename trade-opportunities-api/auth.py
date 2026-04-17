"""
auth.py – Simple JWT-based guest authentication.
"""

import uuid
import logging
from datetime import datetime, timedelta, timezone

import jwt
from config import settings

logger = logging.getLogger(__name__)

ALGORITHM = "HS256"


def create_guest_token() -> str:
    """Creates a signed JWT valid for TOKEN_TTL_MINS minutes."""
    payload = {
        "sub": f"guest-{uuid.uuid4().hex[:8]}",
        "iat": datetime.now(timezone.utc),
        "exp": datetime.now(timezone.utc) + timedelta(minutes=settings.TOKEN_TTL_MINS),
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm=ALGORITHM)
    logger.info("Token created: %s…", token[:12])
    return token


def verify_token(token: str) -> bool:
    """Returns True if the token is valid and not expired."""
    try:
        jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        return True
    except jwt.ExpiredSignatureError:
        logger.warning("Token expired.")
        return False
    except jwt.InvalidTokenError as e:
        logger.warning("Invalid token: %s", e)
        return False
