import cv2
import sys
import imutils

# Load the image
img = cv2.imread("images/flower.png")

if img is None:
    sys.exit("Could not read the image.")

# Get image dimensions
(h, w, d) = img.shape
print("Original Image: width =", w, "height =", h, "depth =", d)

# Task 1: Show Region of Interest (ROI)
startY, endY, startX, endX = 60, 160, 320, 420
roi = img[startY:endY, startX:endX]
cv2.imshow("ROI", roi)
cv2.waitKey(0)

# Task 2: Resize Image to (200, 200)
resized_img = cv2.resize(img, (200, 200))
cv2.imshow("Resized Image", resized_img)
cv2.waitKey(0)

# Task 3: Rotate Image 45 degrees clockwise
rotated_img = imutils.rotate_bound(img, -45)
cv2.imshow("Rotated Image", rotated_img)
cv2.waitKey(0)

# Task 4: Smooth Image with GaussianBlur
blurred_img = cv2.GaussianBlur(img, (11, 11), 0)
cv2.imshow("Blurred Image", blurred_img)
cv2.waitKey(0)

# Task 5: Draw shapes - Rectangle, Circle, Line
output_img = img.copy()
cv2.rectangle(output_img, (50, 50), (200, 200), (0, 255, 0), 2)  # Rectangle
cv2.circle(output_img, (300, 300), 50, (255, 0, 0), -1)           # Circle
cv2.line(output_img, (100, 100), (400, 400), (0, 0, 255), 3)      # Line
cv2.imshow("Drawing Shapes", output_img)
cv2.waitKey(0)

# Task 6: Add Text "Your Name" on the image
cv2.putText(output_img, "Mandar Ambulkar", (10, 30), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.imshow("Image with Text", output_img)
cv2.waitKey(0)

# Task 7: Convert to Grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray_img)
cv2.waitKey(0)

# Task 8: Edge Detection using Canny
edges_img = cv2.Canny(img, 100, 200)
cv2.imshow("Edge Detection", edges_img)
cv2.waitKey(0)

# Task 9: Apply Thresholding
_, threshold_img = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Image", threshold_img)
cv2.waitKey(0)

# Task 10: Detect and Draw Contours
contours, _ = cv2.findContours(threshold_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour_img = img.copy()
cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)
cv2.imshow("Contours", contour_img)
cv2.waitKey(0)

# Save the final image
cv2.imwrite("flower_copy.png", contour_img)

cv2.destroyAllWindows()
