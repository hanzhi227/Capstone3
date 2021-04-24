from flask import Flask, render_template, url_for, request
import numpy as np
from sklearn.datasets import load_iris
import pickle
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from werkzeug.utils import secure_filename
from io import BytesIO
import base64
import random
import os
import cv2
import ffmpy
import time

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static'
# app.config['MAX_CONTENT_PATH']

def convert_avi_to_mp4(avi_file_path, output_name):
    os.system("ffmpeg -i {input} -c:v libx264 -crf 25 -preset fast -y {output}".format(input = avi_file_path, output = output_name))
    return True

def rand():
    return str(np.random.randint(0,8000)).zfill(5)

@app.route('/')
@app.route('/home')
def home(title=None):
    title="Home"
    return render_template("home.html", title=title)

@app.route('/test_set')
def test_set():
    file_num = rand()
    os.system(f"./darknet detector test cfg/custom.data cfg/yolov4-custom.cfg yolov4-custom.weights -dont_show ./cars_test/cars_test/{file_num}.jpg")
    os.system("rm ./static/images/predictions.jpg")
    os.system("cp predictions.jpg ./static/images/")
    return render_template("test_set.html",file_num=file_num)

@app.route('/photo', methods=['POST'])
def photo():
    picture = request.files['photo']
    if os.path.splitext(picture.filename)[1] not in ['.jpg','.png']:
        return render_template('home.html')
    fn = secure_filename('incoming.jpg')
    picture.save(os.path.join(app.config['UPLOAD_FOLDER'],fn))
    return render_template('photo.html', rand=rand())

@app.route('/photo/results', methods=['POST'])
def eval_photo():
    model = request.form['model']
    os.system('rm ./static/predictions.jpg')
    if model == 'car':
        os.system(f"./darknet detector test cfg/custom.data cfg/yolov4-custom.cfg yolov4-custom.weights -dont_show ./static/incoming.jpg")
        os.system('cp predictions.jpg ./static/')
        string = 'Custom Car YOLOv4 Image Result'
    if model == 'coco':
        os.system(f"./darknet detector test cfg/coco.data cfg/yolov4.cfg yolov4.weights ./static/incoming.jpg")
        os.system('cp predictions.jpg ./static/')
        string = 'YOLOv4 COCO Image Result'
    
    return render_template('photo/results.html',rand=rand(),string=string)

@app.route('/video', methods=['POST'])
def video():
    video = request.files['vid']
    if os.path.splitext(video.filename)[1] not in ['.mp4']:
        return render_template('home.html')
    fn = secure_filename('incoming.mp4')
    video.save(os.path.join(app.config['UPLOAD_FOLDER'],fn))
    return render_template('video.html', rand=rand())


@app.route('/video/results', methods=['POST'])
def eval_vid():
    model = request.form['model']
#     os.system('rm ./static/results.mp4')
    if model == 'car':
        os.system('./darknet detector demo cfg/custom.data cfg/yolov4-custom.cfg yolov4-custom.weights -dont_show ./static/incoming.mp4 -i 0 -out_filename results.avi')
        convert_avi_to_mp4('./results.avi','./static/results.mp4')
        string = 'Custom Car YOLOv4 Video Result'
    if model == 'coco':
        os.system('./darknet detector demo cfg/coco.data cfg/yolov4.cfg yolov4.weights -thresh 0.4 -dont_show ./static/incoming.mp4 -i 0 -out_filename results.avi')
        convert_avi_to_mp4('./results.avi','./static/results.mp4')
        string = 'YOLOv4 COCO Video Result'
    time.sleep(2)
    return render_template('video/results.html',rand=rand(),string=string)

@app.route('/predict')
def predict():
    return render_template('predict.html')

if __name__=="__main__":
    app.run(debug=True)