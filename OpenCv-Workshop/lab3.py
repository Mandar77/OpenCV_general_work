# lab3.py

import cv2
import numpy as np

img = cv2.imread("CS5330_F24_Mandar_Ambulkar/OpenCv-Workshop/convert.jpg")

# Resizing
resized_img = cv2.resize(img, (500,500))
cv2.imshow("resized", resized_img)

# Adding text
output_img = cv2.putText(resized_img, "Mandar Ambulkar", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.imshow("Image with Text", output_img)

# Color space conversion
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY", gray_img)

hsV_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsV_img)

cv2.waitKey(0)
cv2.destroyAllWindows()