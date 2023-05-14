import cv2
import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
from keras import models

model = models.load_model('masknet.h5')

def detect(img:np.ndarray, model):
    img=cv2.resize(img,(128,128))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)[0]
    prediction = np.argmax(prediction)
    return prediction
    # if prediction == 0:
    #     return "Mask On!"
    # else:
    #     return "Mask Off / incorrectly"
