# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 22:34:20 2020

@author: Aman Chauhan
"""

from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np

# Keras
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import tensorflow as tf

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

# from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH = 'DenseNet201_20_86.h5'

# Load your trained model
model = load_model(MODEL_PATH)

# dog = ["airport_inside","artstudio","auditorium","bakery","bar","bathroom","bedroom","bookstore","closet",
#               "dentaloffice","elevator","florist","garage","gym","hairsalon","hospitalroom","library","livingroom",
#               "mall","office","poolinside"]
Indoor = ['airport_inside', 'artstudio', 'auditorium',
       'bakery', 'bar', 'bathroom', 'bedroom', 'bookstore', 'bowling',
       'buffet', 'casino', 'children_room', 'church_inside', 'classroom', 'cloister', 'closet', 'clothingstore',
       'computerroom', 'concert_hall', 'corridor', 'deli', 'dentaloffice', 'dining_room', 'elevator',
       'fastfood_restaurant', 'florist', 'gameroom', 'garage', 'greenhouse', 'grocerystore', 'gym', 'hairsalon',
       'hospitalroom', 'inside_bus', 'inside_subway', 'jewelleryshop', 'kindergarden', 'kitchen', 'laboratorywet',
       'laundromat', 'library', 'livingroom', 'lobby', 'locker_room', 'mall', 'meeting_room', 'movietheater', 'museum',
       'nursery', 'office', 'operating_room', 'pantry', 'poolinside', 'prisoncell', 'restaurant', 'restaurant_kitchen',
       'shoeshop', 'stairscase', 'studiomusic', 'subway', 'toystore', 'trainstation', 'tv_studio', 'videostore',
       'waitingroom', 'warehouse', 'winecellar']


def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))
    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    ## Scaling
    x = x / 255
    x = np.expand_dims(x, axis=0)

    preds = model.predict(x)
    # score = tf.nn.softmax(preds)
    print(100 * np.max(preds))
    score = 100 * np.max(preds)

    preds = np.argmax(preds, axis=1)

    preds = Indoor[int(preds)]

    return preds, score


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # prediction
        preds, score = model_predict(file_path, model)
        result = preds.replace('_', ' ').capitalize()
        score = "{:.2f}".format(score)
        result = result + ' ' + f' ( {str(score)} % Prediction score )'
        return result
    return None


if __name__ == '__main__':
    app.run(debug=True)