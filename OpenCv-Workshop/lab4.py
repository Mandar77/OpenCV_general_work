# lab4.py

import cv2
import numpy as np

img = cv2.imread("CS5330_F24_Mandar_Ambulkar/OpenCv-Workshop/convert.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Harris Corner Detection
gray_img = np.float32(gray_img)
harris_corners = cv2.cornerHarris(gray_img, blockSize=20, ksize=3, k=0.04)
harris_corners = cv2.dilate(harris_corners, kernel=None)
img[harris_corners > 0.01 * harris_corners.max()] = [0, 0, 225]
cv2.imshow("Harris corners", img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# SIFT
sift = cv2.SIFT_create()
keypoints, descriptors = sift.detectAndCompute(gray_img, None)
img_keypoints = cv2.drawKeypoints(img, keypoints, None)
cv2.imshow("SIFT keypoints", img_keypoints)

cv2.waitKey(0)
cv2.destroyAllWindows()