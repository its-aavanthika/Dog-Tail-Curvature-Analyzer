from flask import Flask, request, redirect, url_for, send_from_directory, render_template
import os
from utils import extract_tail_region, generate_tail_score
import random

app = Flask(__name__, static_folder='static', template_folder='templates')
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return open('frontend/index.html', encoding='utf-8').read()

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['image']
    if not file:
        return 'No file uploaded'

    filename = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filename)

    tail_path = os.path.join('static', 'tail.png')
    angle = extract_tail_region(filename, tail_path)
    score = generate_tail_score(angle)

    horoscopes = [
        "This tail holds secrets of chaos.",
        "A future of chasing things awaits.",
        "Curves like this aren't made overnight.",
        "The cosmos bows to this tail's geometry."
    ]

    dog_matches = [
        "Courage the Cowardly Dog",
        "Scooby-Doo",
        "Brian Griffin",
        "Bolt"
    ]

    result = {
        'angle': round(angle, 2),
        'score': score,
        'horoscope': random.choice(horoscopes),
        'dog_match': random.choice(dog_matches),
        'tail_path': '/static/tail.png',
        'default_rotation': round(angle, 2)
    }

    return render_template('result.j2', **result)

if __name__ == '__main__':
    app.run(debug=True)
