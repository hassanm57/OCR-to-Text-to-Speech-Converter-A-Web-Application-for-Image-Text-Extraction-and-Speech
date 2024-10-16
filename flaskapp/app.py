from flask import Flask, render_template,request,jsonify
from PIL import Image
import pytesseract
import os
from gtts import gTTS


app = Flask(__name__)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


@app.route('/', methods=['POST','GET'])
def index():
    return render_template ('index.html')

@app.route('/upload', methods=['POST'])


def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image was uploaded'}),400

    file = request.files['image']
    if (file.filename == ''):
        return jsonify({'error': 'No image was selected.'}),400
    
    if not os.path.exists('uploads'):
        os.makedirs('uploads')

    image_path = os.path.join('uploads', file.filename)
    file.save(image_path)

    image = Image.open(image_path)
    ext_text = pytesseract.image_to_string(image)

    os.remove(image_path)

    return (jsonify({'extracted_text': ext_text})), 200

@app.route('/convertToSpeech', methods=['POST']) #route for handling text to speech!

def convert_to_speech():
    data = request.get_json()
    text = data.get('text')

    if not text:
        return jsonify({'error':'no text is provided'}), 400
    
    tts = gTTS(text=text, lang='en')

    #if not os.path.exists('static'):
      #  os.makedirs('static')

    audio_file_path = os.path.join('flaskapp\static','audio.mp3')
    tts.save(audio_file_path)

    return jsonify({'audio_path': '/static/audio.mp3'}), 200
    



if __name__ == '__main__':
    app.run(debug=True)