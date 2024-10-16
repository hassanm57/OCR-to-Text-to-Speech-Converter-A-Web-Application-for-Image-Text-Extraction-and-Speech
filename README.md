
# OCR to Text-to-Speech Converter

## Overview
The **OCR to Text-to-Speech Converter** is a web application that enables users to upload images or capture pictures from their devices to extract text using Optical Character Recognition (OCR) technology. The extracted text can then be converted into speech, allowing users to listen to the content. This project is built using Flask for the backend, Tesseract for OCR, and JavaScript for the frontend interactions.

## Features
- **Image Upload:** Users can upload images or capture them using their device's camera.
- **Text Extraction:** Extracts text from images using Tesseract OCR.
- **Text-to-Speech Conversion:** Converts the extracted text to speech.
- **User-Friendly Interface:** Simple and intuitive design for easy navigation.

## Technologies Used
- **Frontend:**
  - HTML5
  - CSS3
  - JavaScript
- **Backend:**
  - Python
  - Flask
  - Tesseract OCR
- **Libraries:**
  - Pillow (PIL)
  - Fetch API

## Installation Instructions

### Prerequisites
Make sure you have the following installed on your system:
- Python 3.x
- Tesseract OCR (check installation instructions below)

### Step-by-Step Installation
1. **Clone the Repository:**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv env
   ```

3. **Activate the Virtual Environment:**
   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. **Install Required Packages:**
   Create a `requirements.txt` file and add the necessary packages:
   ```
   Flask
   pytesseract
   Pillow
   ```

   Then, run:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up Tesseract OCR:**
   - Download Tesseract from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki) or from the official [Tesseract GitHub repository](https://github.com/tesseract-ocr/tesseract).
   - Follow the installation instructions and ensure the Tesseract executable is added to your system's PATH.
   - Update the `pytesseract.pytesseract.tesseract_cmd` variable in `app.py` to point to your Tesseract executable if necessary.

6. **Run the Application:**
   Execute the following command:
   ```bash
   python app.py
   ```
   Open your web browser and navigate to `http://127.0.0.1:5000` to access the application.

## Usage Instructions
1. **Upload an Image:** Use the provided input field to upload an image or capture one using your device's camera.
2. **Click "Upload Image":** After selecting the image, click the button to send it for text extraction.
3. **View Extracted Text:** The extracted text will appear in the designated textarea.
4. **Convert to Speech:** Press the "Convert To Speech" button to listen to the extracted text.
5. **Playback Controls:** Use the audio controls to play, pause, or stop the audio.

## Contributing
Contributions are welcome! If you have suggestions for improvements or features, please open an issue or create a pull request.

## Acknowledgements
- **Flask** for the lightweight web framework.
- **Tesseract OCR** for its robust text extraction capabilities.
- **Pillow** for image processing functionalities.

---

