#!/usr/bin/env python3
"""Copy entry.txt to /output/entry.txt, byte for byte."""

from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.txt"
OUT_DIR = Path("/output")
OUT = OUT_DIR / "entry.txt"


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(SRC.read_bytes())


if __name__ == "__main__":
    main()
