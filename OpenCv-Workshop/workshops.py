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


cv2.waitKey(0)
cv2.destroyAllWindows()