<p align="center">
  <img width=100% src="https://github.com/hanzhi227/Capstone3/blob/main/images/header.JPG">
</p>


# What Car is That???

------
### Using AI to Determine What Kind of Car is in the Video/Image - Web App

Hanzhi Guo

[LinkedIn](https://www.linkedin.com/in/hanzhi-guo/) | guo.hanzhi95@gmail.com

## >>>[Presentation Video](https://youtu.be/Oq1uYh349Pc)<<<
[Presentation Slides](https://docs.google.com/presentation/d/e/2PACX-1vSdl1l7uCRvTmjy11f4J5vrOp1po1GHL8hUvAB5P0mMBOSc6HA9EYaSoAOVdqFlD-gglx9oY584TUKE/pub?start=false&loop=false&delayms=10000)

------

## Background

------

### Motivation

Object detection is all the rage currently, so I wanted to try my hand at detecting different types of cars with [YOLO Object Detection](https://github.com/AlexeyAB/darknet). YOLO is an extremely fast, state-of-the-art, real-time object detection system. It would be fun to train the AI on normal cars and observing the classification of exotic/uncommon cars, such as the Tesla Truck.

## Data
------
#### [Stanford Cars Dataset](https://www.kaggle.com/eduardo4jesus/stanford-cars-dataset)

The dataset consists of 16,185 images of cars, of which only the 8,144 training images are labeled with car names and bounding boxes. There are 196 unique cars within this dataset. The test set are not labeled with a description.
