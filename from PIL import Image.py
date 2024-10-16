import pytesseract
from PIL import Image

# If Tesseract is not in your PATH, specify the full path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Example of using Tesseract with an image
image = Image.open('figure-65.png')
text = pytesseract.image_to_string(image)
print(text)
