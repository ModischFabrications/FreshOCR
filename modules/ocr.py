import re
from pathlib import Path

import ocrmypdf
import pytesseract as pytesseract

import config


def get_langs() -> str:
    return pytesseract.get_languages()


# this could be a simple subprocess/shell call, not much to gain here
# -> ocrmypdf -O1 -q -l deu --deskew --clean
# not thread-safe!
def ocr_pdf(raw: Path, result: Path, title: str):
    print(f"OCR'ing {raw} into {result}")
    # TODO remove force OCR for real files
    ocrmypdf.ocr(raw, result, deskew=True, optimize=1, clean=True, language=config.OCR_LANG,
                 title=title, author="FreshOCR by Modisch Fabrications", progress_bar=False, force_ocr=True)


def title_from_crop(crop):
    text: str = pytesseract.image_to_string(crop, lang=config.OCR_LANG, config='--psm 6')
    # text = text.replace("\n", " ")
    text = text.split("\n")[0]  # shorter, feel free to skip
    text = re.sub('[./;\t\n]', '', text)  # prevent forbidden chars
    # re.sub(r'[^\w\-_\. ]', '_', filename)
    text.strip()
    return text
