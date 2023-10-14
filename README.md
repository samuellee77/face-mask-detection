# Face Mask Detection

Welcome to **Face Mask Detection Project**! This project was done by Samuel Lee (GitHub: @samuellee77). It uses computer vision to detect whether a person is wearing a face mask or not. The system is built using Python and OpenCV.

## Introduction

This project starts at the onset of the COVID-19 pandemic. It is an innovative solution that aims to reduce the cost and enhance the efficiency of COVID-19 testing. By using computer vision and deep learning model, the system can detect whether a person is wearing a face mask or not. This can be used in a variety of settings, such as schools, hospitals, and public spaces, to ensure that people are following the guidelines for wearing masks. Although the pandemic is slowing down, it is a valuable project to demostrate and may be used in future.

## Installation

To install the necessary dependencies, clone and open this repository. Then, run the following command:

```
pip install -r requirements.txt
```

## Run

To use the GUI powered by Streamlit, run the following command:

```
streamlit run streamlit-app.py
```

Then, a browser tab should pop up, and you can upload the image you want to test if the person in the image is wearing mask. Green rectangle means the person wears mask correctly, red rectangle means the person does not wear mask or wear it incorrectly.

## Resources

- [Kaggle Dataset](https://www.kaggle.com/datasets/andrewmvd/face-mask-detection)
- [OpenCV Docs](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
- [Streamlit Docs](https://docs.streamlit.io/) 