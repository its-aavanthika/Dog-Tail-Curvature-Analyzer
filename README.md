<img width="3188" height="1202" alt="frame (3)" src="https://github.com/user-attachments/assets/517ad8e9-ad22-457d-9538-a9e62d137cd7" />


# Wag-O-Meter 🎯


## Basic Details
### Team Name: Auctrix


### Team Members
- Team Lead: Aavanthika M Nair - Govt. Model Engineering College, Thrikkakara
- Member 2: Arsha Karinkallayi - Govt. Model Engineering College, Thrikkakara

### Project Description
Our project Wag-O-Meter lets users upload a photo of their dog, manually crop the tail, and receive a “Tail Curvature Angle” and “Tail Straightness Score” based on image analysis using OpenCV. Our website also generates a fun dog horoscope, matches the dog to a famous canine character, and provides a certificate for download.

### The Problem (that doesn't exist)
You probably can't describe how much it hurts when something that you do displeases someone and they say "അല്ലേലും പട്ടിയുടെ വാല് പന്തീരാണ്ടു കുഴലിലിട്ടാലും വളഞ്ഞേ ഇരിക്കൂ" which basically implies “No matter how long you try to straighten a dog’s tail, it’ll always stay curved.” But, what if we stopped arguing and just... measured it? Everybody tells you that a dog's tail stays curved, but nobody tells you how to calculate the tail's degree of curvature. Well, no worries - our website does it for you!

### The Solution (that nobody asked for)
Wag-O-Meter - Dog Tail Curvature Analyzer, is a gloriously unnecessary website where you upload a dog photo, crop the tail, and let OpenCV calculate just how crooked it is. You’ll get a Tail Curvature Angle, Tail Straightness Score, a totally made-up dog horoscope, an extra note if you're lucky enough and a certificate to prove your tail has been scientifically analyzed (for no reason at all). Plus, there is an interactive slider for the user to 'straighten' the dog's tail. Umm, all the best using that!

## Technical Details
### Technologies/Components Used

- Python, HTML, CSS, JavaScript
- Flask (Python Web Framework)
- Pillow, Flask, Jinja2, CropperJS
- Browser Developer Tools, VS Code, File System/OS Utilities, Canvas API(HTML5), Local Flask Server, Image viewer/editor


### Implementation

Implementation Overview:

1. Image Upload (Frontend):

* Users upload an image of their dog through the web interface (HTML + JS).
* The image is sent to the backend using a POST request via Flask.

2. Tail Cropping (Manual via Cropper.js):

* The uploaded image is manually cropped by the user to isolate the tail using Cropper.js.
* The cropped image is then sent to the backend.

3. Tail Angle Analysis (OpenCV):

* The backend uses OpenCV to process the cropped image.
* It detects the shape of the tail and calculates its curvature angle.
* This is handled by the analyze\_tail\_angle() function in utils.py.

4. Scoring & Fun Logic:

* A tail straightness score is generated based on the angle.
* Random horoscopes and famous dog comparisons are assigned using Python’s hash function.

5. Rendering the Results (Jinja2 + HTML):

* All this data (angle, score, horoscope, match) is dynamically passed to result.j2.
* The result page displays the angle, image, slider, and fun message.

6. Slider-Based Tail Straightening:

* A slider on the frontend allows users to rotate the tail image.
* After sliding, a message appears: “Nice try. But some things can’t be fixed.”

7. Certificate Generation (Pillow):

* Optionally, users can download a generated certificate with their result embedded.

8. Deployment:

*  Deployed in Render.

# Installation

pip install flask
pip install pillow
pip install open cv

# Run

python app.py

### Project Documentation


# Screenshots (Add at least 3)
![Screenshot1]![alt text](<WhatsApp Image 2025-08-02 at 07.50.18.jpeg>)
Landing Page of the Website

![Screenshot2]![alt text](<WhatsApp Image 2025-08-02 at 07.50.19 (1).jpeg>)
Cropping the Tail using CropperJS

![Screenshot3]![alt text](<WhatsApp Image 2025-08-02 at 07.50.18 (2).jpeg>)
The Tail Curvature Analysis Page


# Diagrams

![Workflow]![alt text](<WhatsApp Image 2025-08-02 at 07.40.07 (1).jpeg>)
This is the workflow of the project.

### Project Demo
# Video

https://drive.google.com/drive/folders/1ngMgWaur_yPdvEwPVUvaW5tFSrBLIqmF
The video basically displays how our website works.


## Team Contributions
- Aavanthika M Nair: Development
- Arsha Karinkallayi: Front-end recommendations

---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--25-25?link=https%3A%2F%2Fwww.tinkerhub.org%2Fevents%2FQ2Q1TQKX6Q%2FUseless%2520Projects)
