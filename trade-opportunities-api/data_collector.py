"""
data_collector.py – Gathers market news for a sector using DuckDuckGo search.
"""

import asyncio
import logging
from datetime import date
from duckduckgo_search import DDGS

logger = logging.getLogger(__name__)

# Search queries run for every sector
QUERY_TEMPLATES = [
    "{sector} India trade opportunities {year}",
    "{sector} India market growth export import {year}",
    "{sector} India government policy investment {year}",
    "{sector} India latest news {year}",
]


class DataCollector:
    """Collects relevant market data snippets for a given sector."""

    async def fetch(self, sector: str) -> dict:
        """
        Returns a dict with:
          - sector: str
          - snippets: list[dict]  (title, body, href)
          - collected_at: str
        """
        year = date.today().year
        queries = [t.format(sector=sector, year=year) for t in QUERY_TEMPLATES]

        snippets = []
        loop = asyncio.get_event_loop()

        for query in queries:
            try:
                # DuckDuckGo search runs in a thread pool to avoid blocking
                results = await loop.run_in_executor(
                    None, self._search, query
                )
                snippets.extend(results)
                logger.info("Query '%s' → %d results", query, len(results))
            except Exception as e:
                logger.warning("Search failed for '%s': %s", query, e)

        # Deduplicate by URL
        seen = set()
        unique = []
        for s in snippets:
            href = s.get("href", "")
            if href not in seen:
                seen.add(href)
                unique.append(s)

        logger.info("Total unique snippets collected: %d", len(unique))

        return {
            "sector": sector,
            "snippets": unique[:20],   # cap at 20 to keep prompt small
            "collected_at": str(date.today()),
        }

    def _search(self, query: str) -> list[dict]:
        """Blocking DuckDuckGo search (called inside executor)."""
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))
        return results
