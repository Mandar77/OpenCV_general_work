# Import necessary libraries
import cv2
import numpy as np

# Load the image
img_path = "D:\\KhouryGithub\\CS5330_F24_Mandar_Ambulkar\\OpenCv-Workshop\\xiao.jpg"
img = cv2.imread(img_path)

# Step 1: Preprocess the image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Step 2: Find contours with different retrieval and approximation modes
# Using RETR_LIST and CHAIN_APPROX_SIMPLE
contours_list, _ = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# Using RETR_TREE and CHAIN_APPROX_NONE for full hierarchy with all contour points
contours_tree, hierarchy_tree = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# Experiment 1: Draw contours with different retrieval modes
output_list = img.copy()
output_tree = img.copy()
cv2.drawContours(output_list, contours_list, -1, (255, 0, 0), 2)  # Draw all contours in blue for RETR_LIST
cv2.drawContours(output_tree, contours_tree, -1, (0, 0, 255), 2)  # Draw all contours in red for RETR_TREE

# Experiment 2: Sort and draw top 5 largest contours by area
sorted_contours = sorted(contours_list, key=cv2.contourArea, reverse=True)[:5]
output_top5 = img.copy()
for contour in sorted_contours:
    cv2.drawContours(output_top5, [contour], -1, (0, 255, 0), 2)  # Draw in green

# Experiment 3: Draw bounding boxes and minimum enclosing circles
output_shapes = img.copy()
for contour in contours_list:
    # Draw bounding rectangle
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(output_shapes, (x, y), (x + w, y + h), (255, 255, 0), 2)
    
    # Draw minimum enclosing circle
    (x_center, y_center), radius = cv2.minEnclosingCircle(contour)
    center = (int(x_center), int(y_center))
    cv2.circle(output_shapes, center, int(radius), (0, 255, 255), 2)

# Step 3: Save the results
cv2.imwrite("output_list_contours.jpg", output_list)
cv2.imwrite("output_tree_contours.jpg", output_tree)
cv2.imwrite("output_top5_contours.jpg", output_top5)
cv2.imwrite("output_shapes.jpg", output_shapes)

# Print saved file paths
print("Images saved with different contour experiments:")
print("RETR_LIST Contours: output_list_contours.jpg")
print("RETR_TREE Contours: output_tree_contours.jpg")
print("Top 5 Largest Contours: output_top5_contours.jpg")
print("Bounding Boxes and Circles: output_shapes.jpg")
