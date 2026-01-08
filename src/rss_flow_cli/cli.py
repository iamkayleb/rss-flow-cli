import argparse
import sys
from pathlib import Path

from .config import add_url, load_config, default_config_path
from .fetcher import fetch_feed, FetchError
from .parser import parse_entries
from .storage import Storage


def cmd_add(args):
    cfg_path = Path(args.config) if args.config else default_config_path()
    add_url(args.url, cfg_path)
    print(f"Added {args.url} to {cfg_path}")


def cmd_sync(args):
    cfg = load_config(args.config)
    if not cfg:
        print("No URLs configured. Use 'rss-flow add <url>' to add feeds.")
        return
    storage = Storage(args.db or ":memory:")
    new_count = 0
    for url in cfg:
        try:
            feed = fetch_feed(url)
        except FetchError as exc:
            print(exc, file=sys.stderr)
            continue
        for entry in parse_entries(feed):
            if storage.save_entry(entry):
                new_count += 1
                title = entry.get("title") or entry.get("link")
                link = entry.get("link")
                print(f"- {title}\n  {link}")
    if new_count == 0:
        print("No new articles found.")


def main(argv=None):
    parser = argparse.ArgumentParser(prog="rss-flow")
    parser.add_argument("--config", help="Path to config.json (optional)")
    parser.add_argument("--db", help="Path to sqlite db file (optional)")

    sub = parser.add_subparsers(dest="cmd")

    p_add = sub.add_parser("add", help="Add feed URL to config")
    p_add.add_argument("url")
    p_add.set_defaults(func=cmd_add)

    p_sync = sub.add_parser("sync", help="Fetch feeds and print new items")
    p_sync.set_defaults(func=cmd_sync)

    args = parser.parse_args(argv)
    if not getattr(args, "func", None):
        parser.print_help()
        return 1
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
