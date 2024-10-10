import cv2
import numpy as np
from numpy import size
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

img = cv2.imread("CS5330_F24_Mandar_Ambulkar/OpenCv-Workshop/convert.jpg")

resized_img = cv2.resize(img, (500,500))
# cv2.imshow("resized", resized_img)

output_img= cv2.putText(resized_img, "Mandar Ambulkar", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
# cv2.imshow("Image with Text", output_img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("GRAY", gray_img)

hsV_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# cv2.imshow("HSV", hsV_img)

gray_img = np.float32(gray_img)
harris_conners= cv2.cornerHarris(gray_img, blockSize=20, ksize=3,k=0.04)
harris_conners= cv2.dilate(harris_conners,kernel=None)
img[harris_conners>0.01 * harris_conners.max()] = [0,0,225]

# cv2.imshow("Harris conners", img)

hist_gray = cv2.calcHist([gray_img], [0], None, [256], [0, 256])

# Plot grayscale histogram
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.plot(hist_gray)
plt.xlim([0, 256])
plt.savefig("CS5330_F24_Mandar_Ambulkar/OpenCv-Workshop/grayhist.jpg")

## Color Histogram

# Split the image into its color channels
b, g, r = cv2.split(img)

# Calculate histograms for each color channel
hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])

# Plot color histograms
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

## 2D Color Histogram

# Calculate 2D color histogram
hist_2d = cv2.calcHist([img], [0, 1], None, [32, 32], [0, 256, 0, 256])

# Plot 2D color histogram
plt.figure()
plt.title('2D Color Histogram (Blue-Green)')
plt.xlabel('Blue')
plt.ylabel('Green')
plt.imshow(hist_2d, interpolation='nearest')
plt.colorbar()

plt.savefig('CS5330_F24_Mandar_Ambulkar/OpenCv-Workshop/output.png')

# Smoothing and Blurring
# Apply averaging (box filter)
blurred_avg = cv2.blur(img, (5, 5))
cv2.imwrite("CS5330_F24_Mandar_Ambulkar/OpenCv-Workshop/blurred_avg.jpg", blurred_avg)

# Apply Gaussian blur
blurred_gauss = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imwrite("CS5330_F24_Mandar_Ambulkar/OpenCv-Workshop/blurred_gauss.jpg", blurred_gauss)

# Apply median blur
blurred_median = cv2.medianBlur(img, 5)
cv2.imwrite("CS5330_F24_Mandar_Ambulkar/OpenCv-Workshop/blurred_median.jpg", blurred_median)

# Apply bilateral filter
blurred_bilateral = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imwrite("CS5330_F24_Mandar_Ambulkar/OpenCv-Workshop/blurred_bilateral.jpg", blurred_bilateral)

# Feature Detection and Matching
# Create SIFT object
sift = cv2.SIFT_create()

# Detect keypoints and compute descriptors
keypoints, descriptors = sift.detectAndCompute(gray_img, None)

# Draw keypoints
img_keypoints = cv2.drawKeypoints(img, keypoints, None)
cv2.imwrite("CS5330_F24_Mandar_Ambulkar/OpenCv-Workshop/sift_keypoints.jpg", img_keypoints)

# Feature Matching with FLANN
# Assuming we have another image to match against
img2 = cv2.imread("CS5330_F24_Mandar_Ambulkar/OpenCv-Workshop/another_image.jpg", 0)
keypoints2, descriptors2 = sift.detectAndCompute(img2, None)

# FLANN parameters
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)

flann = cv2.FlannBasedMatcher(index_params,search_params)
matches = flann.knnMatch(descriptors,descriptors2,k=2)

# Apply ratio test
good_matches = []
for m,n in matches:
    if m.distance < 0.7*n.distance:
        good_matches.append(m)

# Draw matches
img_matches = cv2.drawMatches(img, keypoints, img2, keypoints2, good_matches, None, flags=2)
cv2.imwrite("CS5330_F24_Mandar_Ambulkar/OpenCv-Workshop/flann_matches.jpg", img_matches)

cv2.waitKey(0)
cv2.destroyAllWindows()