 # app.py
import os
import base64
from io import BytesIO
from flask import Flask, render_template, request, send_file
from utils import extract_tail_region, generate_tail_score
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
TAIL_PATH = os.path.join('static', 'tail.png')
CERTIFICATE_PATH = os.path.join('static', 'certificate.png')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return open('frontend/index.html', encoding='utf-8').read()

@app.route('/crop_tail', methods=['POST'])
def crop_tail():
    data_url = request.form['croppedImage']
    header, encoded = data_url.split(",", 1)
    binary_data = base64.b64decode(encoded)
    image = Image.open(BytesIO(binary_data)).convert('RGB')
    image.save(TAIL_PATH)

    angle = extract_tail_region(TAIL_PATH, TAIL_PATH)
    score = generate_tail_score(angle)

    horoscopes = [
        "This tail holds secrets of chaos.",
        "A future of chasing things awaits.",
        "Your tail knows your destiny.",
        "Good boy energy radiates.",
        "This tail is too powerful to tame."
    ]
    matches = [
        "Scooby Doo",
        "Courage the Cowardly Dog",
        "Pluto",
        "Bolt",
        "Santa’s Little Helper"
    ]

    horoscope = horoscopes[hash(encoded) % len(horoscopes)]
    match = matches[hash(encoded[::-1]) % len(matches)]

    return render_template('result.j2', angle=round(angle, 2), score=score,
                           horoscope=horoscope, match=match)

@app.route('/certificate')
def certificate():
    cert = Image.open(CERTIFICATE_PATH).convert('RGB')
    draw = ImageDraw.Draw(cert)
    font = ImageFont.load_default()
    draw.text((100, 100), "Certified Tail Curve Analyzer!", fill=(0, 0, 0), font=font)
    cert_path = os.path.join('static', 'generated_certificate.png')
    cert.save(cert_path)
    return send_file(cert_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
