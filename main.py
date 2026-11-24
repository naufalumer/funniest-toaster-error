#!/usr/bin/env python3
"""Write the funniest toaster error message to entry.txt."""
import os
import sys

LINE = "ERROR E-12: Crumb tray full. I have been eating your crumbs for six months. We need to talk."

def main():
    if not 1 <= len(LINE) <= 120 or not LINE.strip():
        print(f"error: entry must be 1-120 chars, got {len(LINE)}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != LINE:
        print("error: round-trip verify failed: entry.txt does not match LINE", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
