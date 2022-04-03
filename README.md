# FreshOCR

**Bring HelloFresh recipes into the modern, paperless kitchen.**

HelloFresh won't provide PDFs with their boxes, which means that I have a huge stack of paper sitting around. Simple
scans are easier to store, but I want to be able to copy, search and filter them in addition to that.

To enable that you need to OCR the scans for searchability. This is easy to do
with [`ocrmypdf`](https://ocrmypdf.readthedocs.io/en/latest/). Scanning whole batches is still a very manual task
because of splitting and naming the recipes.

This script should minimize that effort, cutting down the time from 3min per recipe to 5min for a whole folder. The core
improvement is automatic OCR for the title of the recipe.

## Process

1. Scan huge list of recipes
   1. scan one side of batch
   2. flip over, scan other side
2. Split/Collate into 2-page PDFs per recipe
3. Extract title from page area using Zonal OCR
4. `ocrmypdf` all pdfs (PDF/A, deskew, OCR, ...) with that title
6. Optional: Copy over and deduplicate with similar recipes
   1. replace old? newer scans likely better

Steps should be executable individually to normalize older entries and integrate better into other tools.

## Installation

Requires Linux or WSL and Python >=3.7.

### External dependencies

Windows: Use WSL (2)

Install dependencies

0. `sudo apt-get update -y && sudo apt-get upgrade -y`
1. `sudo apt install -y ocrmypdf tesseract-ocr-deu`

Feel free to add other languages than `deu` as needed.

Test with

2. `tesseract -h`
3. `ocrmypdf -h`

### Python Dependencies

Copy this project to your folder of choice.

Install python project dependencies with `pipenv install`.

## Execution

Call this python code from the shell that ocrmypdf/tesseract was installed to with `pipenv run ./main.py`.

## Design Decisions

Parallelization: All PDF OCRs could happen in parallel to Zonal OCRs, but it's easier to do both steps in sequence with
parallel runs instead.

`ocrmypdf` can take images, which skips an unnecessary step to unpack PDFs for Zonal OCR. This will probably be faster
too and improve quality, because printers often use outdated compression for PDFs. Only problem might be to keep scan
order for grouping, but this should usually be okay due to increasing timestamps. 



