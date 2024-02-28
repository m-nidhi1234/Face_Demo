from fastapi import FastAPI, UploadFile, File
import cv2
import numpy as np
import random
import cv2
from face_detectors import Ultralight320Detector
from face_detectors.utils import annotate_image



detector = Ultralight320Detector()
app = FastAPI()

def generate_beauty_score(image:any) -> dict:
    faces = detector.detect_faces(image)
    if len(faces) >0:
        random_num = random.randint(1, 10)
        return  {'status':200, 'beauty_score': random_num}
    else:
        return {'status':200, 'beauty_score': "No face found"}

@app.post("/process_image/")
async def process_image(file: UploadFile):
    try:
        image_bytes = await file.read()
        image_array = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        processed_image = generate_beauty_score(image)

        return processed_image
    except Exception as e:
        return {"status": 203, "result":"error" }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
