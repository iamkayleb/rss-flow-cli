import sys
from pathlib import Path

# ensure src is importable
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from rss_flow_cli.storage import Storage


def test_storage_save_and_dedupe(tmp_path):
    db = tmp_path / "test.db"
    s = Storage(str(db))
    entry = {
        "guid": "g1",
        "title": "T",
        "link": "http://x",
        "summary": "S",
        "published": "P",
    }
    assert s.save_entry(entry) is True
    # duplicate should return False
    assert s.save_entry(entry) is False
    # check that one row exists
    cur = s.conn.cursor()
    cur.execute("SELECT COUNT(*) FROM articles")
    assert cur.fetchone()[0] == 1

    # New test for list_entries ordering and limit
def test_list_entries_order_and_limit(tmp_path):
    db = tmp_path / "test2.db"
    s = Storage(str(db))
    for i in range(5):
        s.save_entry({
            "guid": f"g{i}",
            "title": f"T{i}",
            "link": f"http://x/{i}",
            "summary": f"S{i}",
            "published": "",
        })

    items = list(s.list_entries(limit=3))
    assert len(items) == 3
    # items are returned newest first
    assert items[0]["guid"] == "g4"
    assert items[-1]["guid"] == "g2"
