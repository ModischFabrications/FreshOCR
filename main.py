#!/usr/bin/env python3
import sys
from pathlib import Path

from pytesseract import pytesseract

import config
from modules.ocr import ocr_pdf, get_langs
from modules.title_extraction import extract_title


def main():
    print("Starting up, this will take a while...")
    print(f"Langs available: {get_langs()}")
    p_in = Path(config.INPUT_PATH)
    if not p_in.exists(): raise NotADirectoryError("Input is missing")
    p_out = Path(config.OUTPUT_PATH)
    p_out.mkdir(mode=0o777, parents=True, exist_ok=True)

    # TODO do in parallel, encapsulate ocr into threadsafe subprocess
    for f in p_in.glob("*.pdf"):
        title = extract_title(f)
        print(f"Title: {title}")
        ocr_pdf(f, Path(config.OUTPUT_PATH) / (title + ".pdf"), title)

    print("Done.")


if __name__ == '__main__':
    try:
        main()
    except pytesseract.TesseractNotFoundError:
        print("Error: You are missing Tesseract", file=sys.stderr)
    raise SystemExit(1)
