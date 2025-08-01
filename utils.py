import cv2
import numpy as np

def analyze_tail_angle(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return 0.0  # fallback if image not found

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours and fit lines
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    angles = []
    for cnt in contours:
        if len(cnt) >= 5:
            [vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
            angle_rad = np.arctan2(vy, vx)
            angle_deg = np.degrees(angle_rad)[0]
            angles.append(abs(angle_deg))

    if angles:
        average_angle = np.mean(angles)
        return round(average_angle, 2)
    else:
        return 0.0  # No valid contours found
    
def generate_tail_score(angle):
    # A perfect straight tail is 0°, so we reverse the angle to get the score
    score = max(0, 100 - abs(angle))
    return round(score, 2)

