<p align="center">
  <img width=100% src="https://github.com/hanzhi227/Capstone3/blob/main/images/header.JPG">
</p>


# What Car is That???

------
##### Using AI to Determine What Kind of Car is in the Video/Image (Object Detection) - Web App

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

The dataset consists of 16,185 images of cars, of which only the 8,144 images are labeled with car names and bounding boxes. There are 196 unique cars within this dataset.

![](images/data_sample.png)

### Pipeline

From the looks of it, 196 classes is just too specific to do what I am trying to do. How can this model even attempt to recognize unseen data if it is overfit on Toyota Corollas and Ford F-150s? That's why I needed to pipeline the data down significantly to more general body types.

* Group 196 unique car names into more general body types
  * Coupe, Sedan, Convertible, SUV, Truck, Van
  * This would give each class more diversity
  * Creates a more general model that can handel unseen instances

