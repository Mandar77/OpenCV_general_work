# lab5.py

import cv2
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

img = cv2.imread("CS5330_F24_Mandar_Ambulkar/OpenCv-Workshop/convert.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Grayscale Histogram
hist_gray = cv2.calcHist([gray_img], [0], None, [256], [0, 256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.plot(hist_gray)
plt.xlim([0, 256])
plt.savefig("CS5330_F24_Mandar_Ambulkar/OpenCv-Workshop/grayhist.jpg")

# Color Histogram
b, g, r = cv2.split(img)
hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.plot(hist_b, color='b', label='Blue')
plt.plot(hist_g, color='g', label='Green')
plt.plot(hist_r, color='r', label='Red')
plt.xlim([0, 256])
plt.legend()
plt.savefig("CS5330_F24_Mandar_Ambulkar/OpenCv-Workshop/colorhist.jpg")

# 2D Color Histogram
hist_2d = cv2.calcHist([img], [0, 1], None, [32, 32], [0, 256, 0, 256])

plt.figure()
plt.title('2D Color Histogram (Blue-Green)')
plt.xlabel('Blue')
plt.ylabel('Green')
plt.imshow(hist_2d, interpolation='nearest')
plt.colorbar()
plt.savefig('CS5330_F24_Mandar_Ambulkar/OpenCv-Workshop/2dhist.png')

plt.show()