from data_loader import categories
import numpy as np
import os
import matplotlib.pyplot as plt
from PIL import Image

def image_data_loader():
    X = []
    y = []

    for category in categories:
        for file in os.listdir(f'E:/ConvMoNET/Data/{category}s'):
            X.append(np.asarray(Image.open(f'E:/ConvMoNET/Data/{category}s/{file}').convert('L')))
            y.append(category)

    enc = {}
    for i in range(len(categories)):
        enc[categories[i]] = i

    y = list(map(lambda x: enc[x], y))


    X = np.array(X)
    y = np.array(y)

    return X, y
