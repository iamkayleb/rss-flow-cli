import sys
from pathlib import Path

# ensure src is importable
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from rss_flow_cli import config


def test_save_and_load_config(tmp_path):
    cfg = tmp_path / "cfg.json"
    # initially empty
    assert config.load_config(cfg) == []
    config.save_config(["https://example.com/feed.xml"], cfg)
    urls = config.load_config(cfg)
    assert urls == ["https://example.com/feed.xml"]
    # add_url should not duplicate
    config.add_url("https://example.com/feed.xml", cfg)
    assert config.load_config(cfg) == ["https://example.com/feed.xml"]
