#!/usr/bin/env python3
"""CI helper stub: resolve mypy pin.

The upstream reusable workflow expects this script. Provide a no-op
implementation so CI doesn't fail when the file is absent.
"""


def main() -> int:
    print("resolve_mypy_pin: no-op (stub created to satisfy CI)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
