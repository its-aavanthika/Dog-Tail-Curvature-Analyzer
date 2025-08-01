import cv2
import numpy as np

def extract_tail_region(image_path, output_tail_path):
    image = cv2.imread(image_path)
    h_img, w_img = image.shape[:2]

    # Focus on the lower 50% of the image (tail is likely here)
    lower_half = image[h_img//2:, :]
    gray = cv2.cvtColor(lower_half, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 30, 100)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    best_cnt = None
    best_score = 0
    best_angle = 0

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 200 or area > 3000:
            continue

        rect = cv2.minAreaRect(cnt)
        (x, y), (w, h), angle = rect
        aspect_ratio = max(w, h) / (min(w, h) + 1e-5)

        if aspect_ratio > 2.2 and area > best_score:
            best_cnt = cnt
            best_score = area
            best_angle = angle

    if best_cnt is not None:
        x, y, w, h = cv2.boundingRect(best_cnt)
        y += h_img // 2  # Adjust Y to full image coordinates
        tail_crop = image[y:y+h, x:x+w]
        center = (w // 2, h // 2)
        rot_mat = cv2.getRotationMatrix2D(center, best_angle, 1.0)
        rotated = cv2.warpAffine(tail_crop, rot_mat, (w, h), flags=cv2.INTER_LINEAR)
        cv2.imwrite(output_tail_path, rotated)
        return best_angle

    # fallback if nothing found
    fallback = image[-150:, -150:]
    cv2.imwrite(output_tail_path, fallback)
    return 0.0

def generate_tail_score(angle):
    deviation = abs(angle % 180)
    score = max(0, 100 - (deviation / 180) * 100)
    return round(score, 2)
