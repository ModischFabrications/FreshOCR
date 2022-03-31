#!/usr/bin/env python3
import platform

import PIL.Image

from modules.image import pdf_to_img, normalize_size, crop_to_title, preprocess_for_ocr
from modules.ocr import *

# pipenv decided to forbid specification of min versions, so we need to check manually to prevent weird errors
py_version = platform.python_version_tuple()
if int(py_version[0]) < 3 or int(py_version[1]) < 6:
    raise OSError("Python versions older than 3.6 are not supported")


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


def extract_title(f) -> str:
    img = pdf_to_img(f) if (f.suffix == ".pdf") else PIL.Image.open(f)
    crop = crop_to_title(normalize_size(img))
    crop = preprocess_for_ocr(crop)
    title = title_from_crop(crop)
    return title


if __name__ == '__main__':
    main()
