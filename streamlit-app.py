import streamlit as st
import numpy as np
import pandas as pd
import logging as log
from PIL import Image
import matplotlib.pyplot as plt
from keras import models
import cv2
from functions import *

st.title("Face Mask Detection Tool")
st.write("This is a project that was done by Samuel Lee (GitHub: @samuellee77). It is a tool that the user can upload an image and then it will detect whether the people in the images are wearing mask or not or incorrectly.")
st.write("Green rectangle means the person wears mask correctly, red rectangle means the person does not wear mask or wear it incorrectly.")

def main():
    model = models.load_model('masknet.h5')
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    uploaded_file = st.file_uploader("Choose a file", type=["png","jpg","jpeg"])
    if uploaded_file is not None:
        log.info(f"The filename is {uploaded_file.name}")
        image = Image.open(uploaded_file)
        image = np.array(image)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(20,20)
    )
        for (x, y, w, h) in faces:
            crop_img = image[y-5:y+h+5,x-5:x+w+5,]
            label = detect(crop_img, model)
            if label == 0:
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            else:
                cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        st.image(image)

if __name__ == "__main__":
    main()