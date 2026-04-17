"""
session_manager.py – Tracks API usage sessions in memory.
"""

import uuid
import time
import logging
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)


@dataclass
class Session:
    id:         str
    token:      str
    sector:     str
    started_at: float
    finished_at: float = 0.0
    success:    bool   = False


class SessionManager:
    """Stores all sessions in a plain dict (in-memory only)."""

    def __init__(self):
        self._sessions: dict[str, Session] = {}

    def start(self, token: str, sector: str) -> str:
        sid = uuid.uuid4().hex
        self._sessions[sid] = Session(
            id=sid, token=token, sector=sector, started_at=time.time()
        )
        logger.info("Session %s started (sector=%s)", sid[:8], sector)
        return sid

    def finish(self, session_id: str, success: bool) -> None:
        s = self._sessions.get(session_id)
        if s:
            s.finished_at = time.time()
            s.success = success

    def stats(self) -> dict:
        total     = len(self._sessions)
        succeeded = sum(1 for s in self._sessions.values() if s.success)
        failed    = sum(1 for s in self._sessions.values() if s.finished_at and not s.success)
        pending   = total - succeeded - failed

        sector_counts: dict[str, int] = {}
        for s in self._sessions.values():
            sector_counts[s.sector] = sector_counts.get(s.sector, 0) + 1

        return {
            "total_sessions": total,
            "succeeded": succeeded,
            "failed": failed,
            "pending": pending,
            "sectors_analyzed": sector_counts,
        }
