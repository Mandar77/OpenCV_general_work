# lab6.py

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("CS5330_F24_Mandar_Ambulkar/OpenCv-Workshop/convert.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB for matplotlib

# Apply averaging (box filter)
blurred_avg = cv2.blur(img, (5, 5))

# Apply Gaussian blur
blurred_gauss = cv2.GaussianBlur(img, (5, 5), 0)

# Apply median blur
blurred_median = cv2.medianBlur(img, 5)

# Apply bilateral filter
blurred_bilateral = cv2.bilateralFilter(img, 9, 75, 75)

# Display results
plt.figure(figsize=(20, 10))
plt.subplot(231), plt.imshow(img), plt.title('Original')
plt.subplot(232), plt.imshow(blurred_avg), plt.title('Averaging')
plt.subplot(233), plt.imshow(blurred_gauss), plt.title('Gaussian Blur')
plt.subplot(234), plt.imshow(blurred_median), plt.title('Median Blur')
plt.subplot(235), plt.imshow(blurred_bilateral), plt.title('Bilateral Filter')

plt.tight_layout()
plt.savefig('CS5330_F24_Mandar_Ambulkar/OpenCv-Workshop/blurring_results.png')
plt.show()