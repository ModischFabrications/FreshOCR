#!/usr/bin/env python3
import platform

# pipenv decided to forbid specification of min versions, so we need to check manually to prevent weird errors
from modules.ocr import *

py_version = platform.python_version_tuple()
if int(py_version[0]) < 3 or int(py_version[1]) < 6:
    raise OSError("Python versions older than 3.6 are not supported")

from pathlib import Path
import config


def main():
    print("Starting up")
    # print(f"Langs available: {get_langs()}")
    p_in = Path(config.INPUT_PATH)

    # do parallel with workers
    for f in p_in.glob("*.pdf"):
        extract_title(f)
        # ocr_pdf(f)

    print("Done.")


def extract_title(f):
    # TODO skip pdf_to_img for raw inputs
    img = normalize_size(pdf_to_img(f))
    img.show()
    crop = crop_to_title(img)
    crop.show()
    crop = preprocess_for_ocr(crop)
    crop.show()
    # print(f"Title: {title_from_crop(crop)}")


if __name__ == '__main__':
    main()
