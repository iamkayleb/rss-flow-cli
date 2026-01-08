from typing import Dict, List


def parse_entries(feed) -> List[Dict]:
    """Given a feedparser-parsed feed, return a list of dicts with keys:
    'guid', 'title', 'link', 'summary', 'published'
    """
    entries = []
    for e in getattr(feed, "entries", []) or []:
        guid = getattr(e, "id", None) or getattr(e, "guid", None) or getattr(e, "link", None)
        title = getattr(e, "title", "")
        link = getattr(e, "link", "")
        summary = getattr(e, "summary", "") or getattr(e, "description", "")
        published = getattr(e, "published", "")
        entries.append({
            "guid": guid,
            "title": title,
            "link": link,
            "summary": summary,
            "published": published,
        })
    return entries
