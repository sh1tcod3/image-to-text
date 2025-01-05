from PIL import ImageGrab, Image
import pytesseract

def image_from_clipboard_to_text():
    try:

        img = ImageGrab.grabclipboard()

        if isinstance(img, Image.Image):
            print("Image detected in clipboard. Processing...")
 
            text = pytesseract.image_to_string(img)

            print("Extracted Text:")
            print(text)

            return text
        else:
            print("No image found in clipboard. Please copy an image and try again.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")

image_from_clipboard_to_text()
