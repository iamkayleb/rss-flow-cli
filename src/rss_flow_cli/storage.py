import sqlite3
from typing import Dict, Iterator, Optional


class Storage:
    def __init__(self, db_path: str = ":memory:") -> None:
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self._init_db()

    def _init_db(self) -> None:
        cur = self.conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                guid TEXT UNIQUE,
                title TEXT,
                link TEXT,
                summary TEXT,
                published TEXT
            )
            """
        )
        self.conn.commit()

    def has_guid(self, guid: Optional[str]) -> bool:
        if not guid:
            return False
        cur = self.conn.cursor()
        cur.execute("SELECT 1 FROM articles WHERE guid = ?", (guid,))
        return cur.fetchone() is not None

    def save_entry(self, entry: dict) -> bool:
        """Save entry; return True if inserted, False if duplicate."""
        guid = entry.get("guid") or entry.get("link")
        if not guid:
            # For safety, use link as fallback
            guid = entry.get("link")
        if self.has_guid(guid):
            return False
        cur = self.conn.cursor()
        cur.execute(
            "INSERT OR IGNORE INTO articles (guid, title, link, summary, published) VALUES (?, ?, ?, ?, ?)",
            (guid, entry.get("title"), entry.get("link"), entry.get("summary"), entry.get("published")),
        )
        self.conn.commit()
        return cur.rowcount > 0

    def list_entries(self, limit: int = 100) -> Iterator[Dict[str, Optional[str]]]:
        cur = self.conn.cursor()
        cur.execute("SELECT guid, title, link, summary, published FROM articles ORDER BY id DESC LIMIT ?", (limit,))
        for row in cur.fetchall():
            yield {
                "guid": row[0],
                "title": row[1],
                "link": row[2],
                "summary": row[3],
                "published": row[4],
            }
