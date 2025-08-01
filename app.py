# app.py
import os
from flask import Flask, render_template, request, send_file, jsonify
from utils import analyze_tail_angle, generate_tail_score
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
TAIL_PATH = os.path.join('static', 'tail.png')
CERTIFICATE_PATH = os.path.join('static', 'certificate.png')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return open('frontend/index.html', encoding='utf-8').read()

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['dogImage']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    angle = analyze_tail_angle(filepath)
    score = generate_tail_score(angle)

    # Fake horoscope and dog match logic
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

    horoscope = horoscopes[hash(file.filename) % len(horoscopes)]
    match = matches[hash(file.filename[::-1]) % len(matches)]

    return render_template('result.j2', angle=round(angle, 2), score=score,
                           horoscope=horoscope, match=match)

@app.route('/crop-tail', methods=['POST'])
def crop_tail():
    file = request.files['image']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

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