import sys
from pathlib import Path

# ensure src is importable
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import feedparser
from rss_flow_cli import parser


def test_parse_entries():
    sample = """<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0"><channel><title>Example</title>
    <item>
      <title>Article 1</title>
      <link>http://example.com/1</link>
      <description>Summary 1</description>
      <guid>1</guid>
    </item>
    </channel></rss>
    """
    feed = feedparser.parse(sample)
    entries = parser.parse_entries(feed)
    assert len(entries) == 1
    e = entries[0]
    assert e["title"] == "Article 1"
    assert e["link"] == "http://example.com/1"
    assert e["summary"] == "Summary 1"
    assert e["guid"] == "1"
