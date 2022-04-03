import re

import PIL.Image

from modules.image import pdf_to_img, crop_to_title, normalize_size, preprocess_for_ocr
from modules.ocr import title_from_crop


def extract_title(f) -> str:
    img = pdf_to_img(f) if (f.suffix == ".pdf") else PIL.Image.open(f)
    crop = crop_to_title(normalize_size(img))
    crop = preprocess_for_ocr(crop)
    raw_title = title_from_crop(crop)
    title = reformat_title(raw_title)
    return title


# use first line only, prevent forbidden chars, strip whitespace
def reformat_title(text):
    # text = text.replace("\n", " ")
    text = text.split("\n")[0]  # shorter, feel free to skip
    text = re.sub('[./;\t\n]', '', text)  # prevent forbidden chars
    # re.sub(r'[^\w\-_\. ]', '_', filename)
    text.strip()
    return text
