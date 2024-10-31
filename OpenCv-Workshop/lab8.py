# Importing necessary libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Loading the image
img = cv2.imread("D:\\KhouryGithub\\CS5330_F24_Mandar_Ambulkar\\OpenCv-Workshop\\xiao.jpg", cv2.IMREAD_GRAYSCALE)

# Sobel Edge Detection
# Sobel filters in the x and y directions
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)  # x direction
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)  # y direction

# Combine the Sobel x and y images
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

# Canny Edge Detection
canny_edges = cv2.Canny(img, 100, 200)

# Save the images using non-GUI backend
cv2.imwrite("original_image.jpg", img)
cv2.imwrite("sobel_edge_detection.jpg", sobel_combined)
cv2.imwrite("canny_edge_detection.jpg", canny_edges)

# To verify, print the saved file paths
print("Images saved:")
print("Original Image: original_image.jpg")
print("Sobel Edge Detection: sobel_edge_detection.jpg")
print("Canny Edge Detection: canny_edge_detection.jpg")
