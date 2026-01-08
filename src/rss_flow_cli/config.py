import json
from pathlib import Path
from typing import List


def default_config_path() -> Path:
    home = Path.home()
    cfg_dir = home / ".rss-flow-cli"
    cfg_dir.mkdir(parents=True, exist_ok=True)
    return cfg_dir / "config.json"


def load_config(path: Path | None = None) -> List[str]:
    path = Path(path) if path else default_config_path()
    if not path.exists():
        return []
    data = json.loads(path.read_text())
    return data.get("urls", [])


def save_config(urls: List[str], path: Path | None = None) -> None:
    path = Path(path) if path else default_config_path()
    path.write_text(json.dumps({"urls": urls}, indent=2))


def add_url(url: str, path: Path | None = None) -> None:
    urls = load_config(path)
    if url in urls:
        return
    urls.append(url)
    save_config(urls, path)
