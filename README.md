# Clipboard Image to Text Extractor

This tool extracts text from an image in your clipboard using OCR (Optical Character Recognition). It is designed for users who may not have prior programming experience and works efficiently to process clipboard images and display the extracted text.

---

## Features

- Detects images from your clipboard.
- Uses OCR to extract readable text from the image.
- Simple to use, with minimal setup.

---

## Prerequisites

Before using the tool, ensure the following are installed on your computer:

1. **Python** (Version 3.8 or later)
   - [Download Python](https://www.python.org/downloads/)
2. **Tesseract OCR**
   - Install Tesseract OCR:
     - For Windows: [Tesseract Installer](https://github.com/UB-Mannheim/tesseract/wiki)
     - For macOS: Use `brew install tesseract` (requires [Homebrew](https://brew.sh/))
     - For Linux: Use your package manager (e.g., `sudo apt install tesseract-ocr`)

---

## Installation

1. Download the script file (`image_to_text.py`) or copy the code from this repository.
2. Open a terminal or command prompt and run the following commands:

```bash
# Install required Python packages
pip install pillow pytesseract
```

 ## Usage
### Run the script:

Open your terminal or command prompt and navigate to the folder containing the script.
Run the script using:
```bash
python image_to_text.py
```
Copy an image to the clipboard:

Take a screenshot or copy an image to your clipboard.
View the extracted text:

The script will detect the image in the clipboard and display the extracted text.
