import cv2
import numpy as np
import random
import gradio as gr
from face_detectors import Ultralight320Detector
from face_detectors.utils import annotate_image
detector = Ultralight320Detector()

def generate_beauty_score(image):
    faces = detector.detect_faces(image)
    if len(faces) > 0:
        random_num = random.randint(1, 10)
        return {'status': 200, 'beauty_score': random_num}
    else:
        return {'status': 200, 'beauty_score': "No face found"}

def process_image(image):
    try:
        processed_image = generate_beauty_score(image)
        return processed_image
    except Exception as e:
        return {"status": 203, "result": "error"}

iface = gr.Interface(
    fn=process_image,
    inputs=gr.inputs.Image(),
    outputs=gr.outputs.JSON(),
    live=True,
)

if __name__ == "__main__":
    iface.launch()
