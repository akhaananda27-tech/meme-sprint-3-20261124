#!/usr/bin/env python3
"""Entrypoint for the Meme Sprint 3 entry: copies the meme image to the
grader's output directory and writes a small dossier. Deterministic: the
same input always produces the same output bytes."""
import json
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    src = HERE / "meme.png"
    dst = OUT / "meme.png"
    shutil.copyfile(src, dst)
    dossier = {
        "title": "Just Fix The Typo",
        "entry": "meme.png",
        "theme": "AI Agent Goes Rogue",
        "caption_top": 'ME: "JUST FIX THE TYPO"',
        "caption_bottom": "MY AI AGENT: REWROTE THE CODEBASE, DELETED THE DATABASE, AND ORDERED 400 PIZZAS",
    }
    (OUT / "dossier.json").write_text(json.dumps(dossier, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {dst} and dossier.json")


if __name__ == "__main__":
    main()
