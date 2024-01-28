from flask import Flask, request, render_template, jsonify
from flask import render_template
import base64, os, random
from uuid import uuid4
from MLModel.data_load import dec
from tensorflow import keras
from model import model, predict_
import numpy as np

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main_page.html')

@app.route("/info")
def info():
    return render_template('info_page.html')

@app.route("/guesso")
def guesso_render():
    return render_template('guesso_page.html')


@app.route("/guesso", methods=["POST", "GET"])
def predict_digit():
    image = request.get_json(silent=True)['image'].split(",")[1]
    image_data = base64.urlsafe_b64decode(image)


    prediction = predict_(image_data)
    print(np.argmax(prediction))

    response = { 
        "prediction": dec[np.argmax(prediction)]
    }

    return jsonify(response)
