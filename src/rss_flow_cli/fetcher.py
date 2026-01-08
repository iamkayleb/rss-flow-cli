from typing import Optional

import requests
import feedparser


class FetchError(Exception):
    pass


def fetch_feed(url: str, timeout: int = 10) -> feedparser.FeedParserDict:
    """Fetch RSS/Atom feed from URL and return parsed feedparser object.

    Raises FetchError on network/fetch failures.
    """
    try:
        resp = requests.get(url, timeout=timeout, headers={"User-Agent": "rss-flow-cli/0.1"})
        resp.raise_for_status()
    except Exception as exc:
        raise FetchError(f"Failed to fetch {url}: {exc}") from exc

    parsed = feedparser.parse(resp.content)
    return parsed
