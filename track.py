import cv2
from ultralytics import YOLO
import numpy as np
from collections import defaultdict
# Load the YOLOv8 model
model = YOLO('yolov8n.pt')

# Open the video file
video_path = "people.mp4"
cap = cv2.VideoCapture(video_path)

track_history = defaultdict(lambda: [])

# Loop through the video frames
while cap.isOpened():
    success, frame = cap.read() # Read frames
    if success:
        # Run YOLOv8 tracking on the frame, persisting tracks between frames
        results = model.track(frame, persist=True)
        
        # Boxes from results
        boxes = results[0].boxes.xywh.cpu()
        track_ids = results[0].boxes.id.int().cpu().tolist()

        # Visualize the results on the frame
        annotated_frame = results[0].plot()
       
        # Loop through each box 
        for box, track_id in zip(boxes, track_ids):
            x, y, w, h = box
            track = track_history[track_id]

            track.append((float(x), float(y)))  # x, y center point
            # if camera is moving subtract postion of camera
            # position_cam.x,position_cam.y = (position_cam.x+h,position_cam.y+w)
            # track.append((float(x)-position_cam.x),(float(y)-position_cam.y)) # essentially TF from odom to camera

            if len(track) > 30:  # retain 90 tracks for 90 frames
                track.pop(0)

            # Draw the tracking lines
            points = np.hstack(track).astype(np.int32).reshape((-1, 1, 2))
            cv2.polylines(annotated_frame, [points], isClosed=False, color=(230, 230, 230), thickness=10)

        # Display the annotated frame
        cv2.imshow("YOLOv8 Tracking", annotated_frame)

        # Break the loop if 'q' is pressed
print(cap.isOpened())
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()

