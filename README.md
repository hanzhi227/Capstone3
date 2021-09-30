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

[Weights and cfg file](https://drive.google.com/drive/folders/1-4GN9HdRTMGXNbUb_CsHPk9xl3DQsI79?usp=sharing) need to be placed in /darknet/cfg/ after running the makefile.

## Background

------

### Motivation

Object detection is all the rage currently, so I wanted to try my hand at detecting different types of cars with [YOLO Object Detection](https://github.com/AlexeyAB/darknet). YOLO is an extremely fast, state-of-the-art, real-time object detection system. It would be fun to train the AI on normal cars and observing the classification of exotic/uncommon cars, such as the Tesla Truck.

## Data
------
#### [Stanford Cars Dataset](https://www.kaggle.com/eduardo4jesus/stanford-cars-dataset)

The dataset consists of 16,185 images of cars, of which only the 8,144 images are labeled with car names and bounding boxes. There are 196 unique cars within this dataset.

<p align="center">
  <img src="https://github.com/hanzhi227/Capstone3/blob/main/images/data_sample.png">
</p>

### Pipeline

From the looks of it, 196 classes is just too specific to do what I am trying to do. How can this model even attempt to recognize unseen data if it is overfit on Toyota Corollas and Ford F-150s? That's why I needed to pipeline the data down significantly to more general body types.

* Group 196 unique car names into more general body types
  * Coupe, Sedan, Convertible, SUV, Truck, Van
  * This would give each class more diversity
  * Creates a more general model that can handel unseen instances

### Training

After the data was pipelined into 6 classes, I trained the model on a Google Colab GPU instance for ~20 hours. With the accuracy at 100% on the training data, I was ready to see the try its hand at exotic cars!

<p align="center">
  <img src="https://github.com/hanzhi227/Capstone3/blob/main/images/training.JPG">
</p>


## Flow of Web App

The user can upload any image (png or jpg) or video (mp4) via the landing page. Then the user picks if they want to use the COCO dataset weights or my custom car dataset weights. After they press "process image" or "process video", the image or video is sent to the python backend where it goes throught the YOLOv4 framework on the GPU-backed AWS instance. Videos will take longer to process depending on size of the file, but images will process quite fast. After the file is processed, the final page of the web app will display back the original image or even video with all of the bounding boxes surrounding the objects it detects and classifying what it is i.e. sedan, coupe, convertible, SUV, truck, Van, etc.


#### Flow Diagram of User and Data

<p align="center">
  <img src="https://github.com/hanzhi227/Capstone3/blob/main/images/flow.JPG">
</p>



#### Landing Page

<p align="center">
  <img src="https://github.com/hanzhi227/Capstone3/blob/main/images/site1.JPG">
</p>



#### Model Selection Page

<p align="center">
  <img src="https://github.com/hanzhi227/Capstone3/blob/main/images/site2.JPG">
</p>




#### Results Page

<p align="center">
  <img src="https://github.com/hanzhi227/Capstone3/blob/main/images/site3.JPG">
</p>


#### Lancia Prediction

<p align="center">
  <img src="https://github.com/hanzhi227/Capstone3/blob/main/images/lancia.JPG">
</p>


#### Lightning McQueen Prediction

<p align="center">
  <img src="https://github.com/hanzhi227/Capstone3/blob/main/images/lightning.JPG">
</p>

------

### Conclusion

The results are quite satisfactory. My goal of creating a fun, interactive web app was a huge success. The model actually correctly classified Lightning McQueen and the Tesla Cyber Truck. The Lancia's door is the front windshield so even I am uncertain of what type of car it is, but it sure does look like it can be a coupe!

If you want to see it process videos, please check out my [presentation video](https://youtu.be/Oq1uYh349Pc).
