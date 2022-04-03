import subprocess
from pathlib import Path

import ocrmypdf
import pytesseract as pytesseract

import config


def get_langs() -> str:
    return pytesseract.get_languages()


# not thread-safe! check ocr_pdf_cli, that one allows parallelization
def ocr_pdf(raw: Path, result: Path, title: str):
    print(f"OCR'ing {raw} into {result}")
    # TODO remove force OCR for real files
    # TODO optimize, still 1.37x larger and with different deskew than cli version
    ocrmypdf.ocr(raw, result, deskew=True, optimize=1, clean=True, language=config.OCR_LANG,
                 title=title, author="FreshOCR by Modisch Fabrications", progress_bar=False, force_ocr=True)


def ocr_pdf_cli(raw: Path, result: Path, title: str):
    print(f"OCR'ing {raw} into {result}, using cli")
    return_code = subprocess.run(["ocrmypdf", "-O1", "-q", "--deskew", "--clean",
                                  f"-l {config.OCR_LANG}",
                                  f"--title {title}",
                                  f"--author 'FreshOCR by Modisch Fabrications'",
                                  raw.absolute(), result.absolute()])
    print(return_code)


def title_from_crop(crop):
    text: str = pytesseract.image_to_string(crop, lang=config.OCR_LANG, config='--psm 6')
    return text
