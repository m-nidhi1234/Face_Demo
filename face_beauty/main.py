from face_detectors import Ultralight320Detector
from face_detectors.utils import annotate_image
import cv2

detector = Ultralight320Detector()

image = cv2.imread("image.png")

faces = detector.detect_faces(image)
print(faces)
image = annotate_image(image, faces, width=3)

cv2.imshow("view", image)
cv2.waitKey(100000)