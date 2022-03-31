from pathlib import Path

from PIL import ImageFilter
from pikepdf import Pdf, PdfImage

import config


# pikepdf, could be omitted if scanning to images
def pdf_to_img(path: Path):
    pdf = Pdf.open(path)
    p0_images = pdf.pages[0].images
    pdfimage = PdfImage(p0_images[list(p0_images.keys())[0]])
    img = pdfimage.as_pil_image()
    return img


# normalize_size to 300 dpi/A4 for crops
def normalize_size(img):
    print(f"Base Size: {img.size} Base DPI: {img.info['dpi'][0]}")
    img = img.resize((3508, 2480))
    return img


def crop_to_title(img):
    crop = img.crop(config.CROP_AREA_TITLE)
    return crop


# this might be worse because tesseract can do it better
def preprocess_for_ocr(img):
    proc_img = img.convert('L')  # grayscale
    proc_img = proc_img.filter(ImageFilter.MedianFilter())  # a little blur
    proc_img = proc_img.point(lambda x: 0 if x < 200 else 255)  # threshold (binarize)
    return proc_img
