import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

cap = cv2.VideoCapture('./video/videoplayback.mp4')
count = 0
previous_position = {}

while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    results = model.track(frame, persist = True)

    line_y = 180

    
       
    if results[0].boxes.id is not None:
       for box in results[0].boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        center_y = (y1+y2)/2

        vehicle_id = int(box.id)
        
        if vehicle_id in previous_position:
           if previous_position[vehicle_id] < line_y and  center_y > line_y:
            count+=1

        previous_position[vehicle_id] = center_y

        

    cv2.putText(frame,f"count:{count}",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)      
    cv2.line(frame,(0,line_y),(640,line_y),(255,0,0),2)
    cv2.imshow("frame",frame)  

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
