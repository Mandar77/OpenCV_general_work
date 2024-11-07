# Import necessary libraries
import cv2
import numpy as np

# Load the image
img_path = "D:\\KhouryGithub\\CS5330_F24_Mandar_Ambulkar\\OpenCv-Workshop\\xiao.jpg"
img = cv2.imread(img_path)

# Step 1: Preprocess the image
# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to obtain a binary image
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Step 2: Find contours
# Use RETR_EXTERNAL to retrieve only outermost contours and CHAIN_APPROX_SIMPLE for approximation
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Step 3: Draw contours on the original image
# Draw all contours (-1) in green color with a thickness of 2
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

# Step 4: Save the result
output_path = "contours_output.jpg"
cv2.imwrite(output_path, img)

# Print the output path to verify
print("Contours image saved at:", output_path)