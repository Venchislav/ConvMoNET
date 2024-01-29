from PIL import Image
import os, io
import numpy as np
from tensorflow import keras
from tensorflow.keras import Sequential, layers
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from MLModel.data_loader import categories

num_classes = len(categories)
IMG_SIZE = 28

model = keras.models.load_model('E:\ConvMoNET\MLModel\model_cnn.h5')


def predict_(image_data):
    image = Image.open(io.BytesIO(image_data))
    image = image.convert("L")

    image = image.resize((28, 28))

    dataset_image = 'E:/ConvMoNET/Data/facess/6668425537519616-True.jpg'
    dataset_image = Image.open(dataset_image)
    dataset_image = dataset_image.resize((28, 28))
    dataset_image.save('E:\ConvMoNET\TestImages\here-dataset.png')
    image.save('E:\ConvMoNET\TestImages\here.png')

    image = np.array(image)

    image = image.reshape(1, 28, 28, 1)
    image = image.astype(np.float32)
    prediction = model.predict(image)

    return prediction
