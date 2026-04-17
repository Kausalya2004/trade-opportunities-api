"""
rate_limiter.py – In-memory sliding-window rate limiter.
"""

import time
import logging
from collections import defaultdict, deque

logger = logging.getLogger(__name__)


class RateLimiter:
    """
    Allows at most `max_requests` per token in the last `window_seconds` seconds.
    Uses an in-memory deque — resets when the server restarts.
    """

    def __init__(self, max_requests: int = 10, window_seconds: int = 60):
        self.max_requests  = max_requests
        self.window        = window_seconds
        self._history: dict[str, deque] = defaultdict(deque)

    def _clean(self, token: str) -> None:
        """Remove timestamps that are outside the sliding window."""
        cutoff = time.time() - self.window
        q = self._history[token]
        while q and q[0] < cutoff:
            q.popleft()

    def allow(self, token: str) -> bool:
        """Returns True (and records the request) if allowed; False if rate-limited."""
        self._clean(token)
        q = self._history[token]
        if len(q) >= self.max_requests:
            logger.warning("Rate limit hit for token %s…", token[:8])
            return False
        q.append(time.time())
        return True

    def remaining(self, token: str) -> int:
        """How many requests the token can still make right now."""
        self._clean(token)
        return max(0, self.max_requests - len(self._history[token]))
