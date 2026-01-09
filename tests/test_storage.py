import sys
from pathlib import Path

# ensure src is importable
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from rss_flow_cli.storage import Storage


def test_storage_save_and_dedupe(tmp_path):
    db = tmp_path / "test.db"
    s = Storage(str(db))
    entry = {"guid": "g1", "title": "T", "link": "http://x", "summary": "S", "published": "P"}
    assert s.save_entry(entry) is True
    # duplicate should return False
    assert s.save_entry(entry) is False
    # check that one row exists
    cur = s.conn.cursor()
    cur.execute("SELECT COUNT(*) FROM articles")
    assert cur.fetchone()[0] == 1
