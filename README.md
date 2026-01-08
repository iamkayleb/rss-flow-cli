# rss-flow-cli ✅

Command-line RSS tracker that remembers articles between runs.

## Features

- Add RSS/Atom feed URLs to a config file
- Run `rss-flow sync` to fetch feeds and print new articles since the last run
- Deduplicates articles using a SQLite database

## Architecture

- `src/rss_flow_cli/fetcher.py`: Fetches RSS with `requests` and parses with `feedparser`
- `src/rss_flow_cli/parser.py`: Cleans and extracts `title`, `link`, `summary`, `guid`, `published`
- `src/rss_flow_cli/storage.py`: Stores articles in SQLite and prevents duplicates
- `src/rss_flow_cli/cli.py`: CLI implemented with `argparse`

## Quickstart

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Add a feed URL:

```bash
python -m rss_flow_cli.cli add https://example.com/feed.xml
```

3. Sync and show new articles:

```bash
python -m rss_flow_cli.cli sync
```

## Running tests

```bash
pip install -r requirements.txt
pytest
```

## Notes

- By default the config file is stored at `~/.rss-flow-cli/config.json`.
- You can override the config or DB path with `--config` and `--db` flags.

Contributions welcome! ✨
