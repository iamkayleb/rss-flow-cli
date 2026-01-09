#!/usr/bin/env python3
"""CI helper stub: sync test dependencies.

The upstream reusable workflow expects this script. Provide a small
no-op implementation so CI doesn't fail when the file is absent.
"""


def main() -> int:
    print("sync_test_dependencies: no-op (stub created to satisfy CI)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
