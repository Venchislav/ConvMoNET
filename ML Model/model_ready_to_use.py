from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from tensorflow.keras.optimizers import Adam
from data_loader import categories
import numpy as np
from PIL import Image
import tensorflow as tf
from data_load import dec

IMG_SIZE = 28
num_classes = len(categories)

def create_model():
    model = Sequential([
        layers.Rescaling(1./255, input_shape=(IMG_SIZE, IMG_SIZE, 1)),
        layers.Conv2D(30, (5, 5), activation='relu'),
        layers.MaxPool2D(pool_size=(2, 2)),
        layers.BatchNormalization(),
        layers.Conv2D(15, (3, 3), activation='relu'),
        layers.MaxPool2D(pool_size=(2, 2)),
        layers.BatchNormalization(),

        layers.Flatten(),

        layers.Dense(256, activation='relu'),
        layers.Dropout(0.2),
        layers.Dense(64, activation='relu'),
        layers.Dropout(0.3),
        layers.Dense(num_classes, activation='softmax')
    ])

    model.compile(
        optimizer=Adam(learning_rate=0.01),
        loss=SparseCategoricalCrossentropy(),
        metrics=['accuracy']
    )

    return model


model = create_model()
model.load_weights('E:\ConvMoNET\ML Model\model_saves')
image = np.asarray(Image.open('E:/ConvMoNET/TestImages/Cat.png').convert('L'))
image = [image]
image = np.expand_dims(image, 3)
image = tf.image.resize(image, (28, 28))
print(image.shape)

test_pred = model.predict(image)
print(dec[np.argmax(test_pred)])