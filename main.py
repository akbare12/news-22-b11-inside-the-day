#!/usr/bin/env python3
"""Copy program for the news-image-20261122 entry (INSIDE THE DAY).

Reproduces entry.png byte-identically into the output directory.
Standard library only; no network.
"""
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")

EXPECTED_SHA256 = "8a5767535811cfcad91689d7c2be7340d091e9a8f8bbca0e2125a61711a7758b"
EXPECTED_BYTES = 203674


def main():
    with open(SRC, "rb") as f:
        data = f.read()
    assert data[:8] == b"\x89PNG\r\n\x1a\n", "entry.png is not a PNG"
    # IHDR: width and height are the first 8 bytes after the 8-byte
    # signature + 4-byte length + 4-byte "IHDR" tag (offset 16).
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    assert (width, height) == (1024, 1024), "entry.png must be 1024x1024"
    assert len(data) == EXPECTED_BYTES, "entry.png size mismatch"
    digest = hashlib.sha256(data).hexdigest()
    assert digest == EXPECTED_SHA256, "entry.png sha256 mismatch"
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    with open(DST, "rb") as f:
        copied = f.read()
    assert hashlib.sha256(copied).hexdigest() == EXPECTED_SHA256
    print(f"wrote {DST} ({len(copied)} bytes, sha256 {EXPECTED_SHA256})")


if __name__ == "__main__":
    main()
