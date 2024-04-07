# ERIC Robotics Perception task

### RUN
```sh
python3 track.py
```
---
### Prerequisites
  1. yolov8
  2. Opencv
  3. python3
---
#### AIM: To track objects in realtime using YOLOv8 \

#### Introduction
We use YOLOv8 to track/detect objects in realtime. YOLOv8 is a deep learning object detection model. \
We use its python API to model the frames of a video. \

There are diffrent models from YOLOv8

**YOLOv8n (Nano)**: The smallest and fastest. Ideal for super real-time applications with limited compute power \
**YOLOv8s (Small)**: Slightly larger than Nano, with increased accuracy. \
**YOLOv8m (Medium)**: A well-rounded option, delivering a solid blend of accuracy and speed. \
**YOLOv8l (Large)**: The biggest and most accurate. Primarily designed for use cases where top-tier accuracy is paramount. \
**YOLOv8x (Extra Large)**: The absolute performance beast. This model pushes the boundaries of accuracy but be aware, it's the slowest due to its complexity. 

This code use YOLOv8n 
Object detection capabilites is exted to track objects.\
This is done by BoT-SORT or ByteTrack \
We use the default BoT-SORT to: 
  1. track multiple objects 
  2. Each objects has unique identifcation 
---
#### Explanation: 
  Iterate over each frame of video: \
    Call model.track(frame) function \
    plot the results on to image \
    store the boxes, track id from the results \
    for each trackid \
      plot a point on the image at box.center 

  display the image 

---
#### Application 
This code has an direct application in robotics. \
We can track objects (people) from stationary objects for an autnomous ground vehcicle \

Example: \
Using a sample based planner, The bot samples a state (x,y) over state space. \
Given the position of the objects over time dt, we can estimate the speed of the objects, thus determining the position of the object at time T1 in the **future**! \
The path planner plan path according to this moving object to avoid near colision. 


#
