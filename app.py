import os
import time
from flask import Flask, render_template, request, send_file
from utils import analyze_tail_angle, generate_tail_score
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__, template_folder='templates')

UPLOAD_FOLDER = 'uploads'
STATIC_FOLDER = 'static'
CERTIFICATE_TEMPLATE = os.path.join(STATIC_FOLDER, 'certificate_template.png')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    # 🧹 Clean previous uploads
    for f in os.listdir(UPLOAD_FOLDER):
        os.remove(os.path.join(UPLOAD_FOLDER, f))
    print("🧹 Cleaned uploads folder.")

    # 📥 Save the new image
    file = request.files['dogImage']
    filename = file.filename or f"tail_{int(time.time())}.png"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    print(f"✅ Saving: {filename}")

    # 🧠 Analyze it
    angle = analyze_tail_angle(filepath)
    score = generate_tail_score(angle)

    # 🐶 Fun stuff
    horoscopes = [
        "This tail holds secrets of chaos.",
        "A future of chasing things awaits.",
        "Your tail knows your destiny.",
        "Good boy energy radiates.",
        "This tail is too powerful to tame."
    ]
    matches = [
        "Scooby Doo",
        "Arjun from CID Moosa",
        "Pluto from Mickey Mouse",
        "Bolt",
        "Laika"
    ]

    horoscope = horoscopes[hash(filename) % len(horoscopes)]
    match = matches[hash(filename[::-1]) % len(matches)]

    # 🥚 Easter eggs
    extra_note = ""
    if 68 <= angle <= 70:
        extra_note = "Nice. Very nice."
    elif angle > 135:
        extra_note = "This is basically a spiral. Time traveler confirmed."
    elif match == "Pluto from Mickey Mouse":
        extra_note = "Did you know Pluto isn't a planet anymore?"

    # 🖼️ Save a copy to static folder
    static_tail_path = os.path.join(STATIC_FOLDER, filename)
    Image.open(filepath).save(static_tail_path)

    # 🪪 Generate new certificate each time from clean template
    cert = Image.open(CERTIFICATE_TEMPLATE).convert('RGB')
    draw = ImageDraw.Draw(cert)
    font = ImageFont.load_default()

    # Dynamically write details
    draw.text((100, 100), "Certified Tail Curve Analyzer!", fill=(0, 0, 0), font=font)
    draw.text((100, 130), f"Tail Angle: {round(angle, 2)}°", fill=(0, 0, 0), font=font)
    draw.text((100, 160), f"Tail Score: {score}%", fill=(0, 0, 0), font=font)
    draw.text((100, 190), f"Horoscope: {horoscope}", fill=(0, 0, 0), font=font)
    draw.text((100, 220), f"Dog Match: {match}", fill=(0, 0, 0), font=font)
    draw.text((100, 250), f"Issued: {time.strftime('%Y-%m-%d %H:%M:%S')}", fill=(0, 0, 0), font=font)

    # Unique filename
    cert_filename = f"certificate_{int(time.time() * 1000)}.png"
    cert_path = os.path.join(STATIC_FOLDER, cert_filename)
    cert.save(cert_path)



    return render_template('result.j2', angle=round(angle, 2), score=score,
                           horoscope=horoscope, match=match,
                           tail_image=filename, certificate_image=cert_filename,
                           extra_note=extra_note)

@app.route('/certificate/<filename>')
def certificate(filename):
    return send_file(os.path.join(STATIC_FOLDER, filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
