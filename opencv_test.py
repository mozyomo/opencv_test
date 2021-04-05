import cv2
import matplotlib.pyplot as plt

image = cv2.imread("marchantia.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)