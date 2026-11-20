#!/usr/bin/env python3
"""news-image-20261120: write the finished front page to /output/entry.png.

Standard library only. The image is the committed entry.png, drawn
offline at build time with PIL; this program only copies those exact
bytes to the grader's output directory. No network, no randomness:
two runs produce byte-identical output.
"""

import os
import shutil
import sys

MAX_BYTES = 1048576  # 1 MiB


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.environ.get(
        "MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    if size > MAX_BYTES:
        print(f"error: {dst} is {size} bytes, over the 1 MiB limit",
              file=sys.stderr)
        return 1
    print(f"wrote {dst}: {size} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
