import cv2
from datetime import datetime
import os

def capture_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        image_path = f'static/images/{timestamp}.png'
        cv2.imwrite(image_path, frame)
    cap.release()
    return image_path if ret else None

# Ensure the images directory exists
if not os.path.exists('static/images'):
    os.makedirs('static/images')
