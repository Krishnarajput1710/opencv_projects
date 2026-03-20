# opencv_projects
This is my first opencv project 

# It's a simple object counter here we are counting number of cars paas through.
I am using 'yolov8n.pt' model to detect object 
in this project I am performing inference.
the model provide coordinates and gives id to vehicles, then the cordinates are compared in each frames to identify if the vehicle has crossed the line if yes then the count will increase.

# Limitations 
It certainly not accurate model as it can miss some cars which pass by
It only checks whether the car has pass through the virtual line if not it won't be count in.

# What I Learned
I learned that results contains bounding box coordinates in xyxy format
I understand the difference between a for loop running every frame vs variables declared outside the loop
I also got to know what track loss is and why it causes missed detections
I also learned what persist=True does in YOLO tracking

## How to Run
pip install ultralytics opencv-python
Add your video file to /video/videoplayback.mp4
python counter.py
Press q to quit
