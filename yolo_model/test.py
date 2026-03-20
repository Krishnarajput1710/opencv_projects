import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')
cap = cv2.VideoCapture('./video/videoplayback.mp4')
ret, frame = cap.read()

results = model(frame)
print(type(results))
print(results[0].boxes)
cap.release()