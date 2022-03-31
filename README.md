# FreshOCR

Requires Python >=3.7

# Installation

## External dependencies

Windows: Use WSL, manual installation seems to be too cumbersome

0. `sudo apt-get update -y && sudo apt-get upgrade -y`
1. `sudo apt install -y ocrmypdf tesseract-ocr-deu`
   Feel free to add other languages as needed.

Test with

2. `tesseract -h`
3. `ocrmypdf -h`

## Python Dependencies

Install python project with

1. `pip install pipenv`
2. `pipenv install`

# Execution

Call this python code from the shell that ocrmypdf/tesseract was installed to.

pipenv run ./main.py




