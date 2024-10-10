# lab2.py

import cv2

# Loading images
img = cv2.imread("CS5330_F24_Mandar_Ambulkar/OpenCv-Workshop/convert.jpg")
gray_img = cv2.imread("CS5330_F24_Mandar_Ambulkar/OpenCv-Workshop/convert.jpg", cv2.IMREAD_GRAYSCALE)

# Displaying images
cv2.imshow("Original", img)
cv2.imshow("GRAY", gray_img)

# Saving images
cv2.imwrite("CS5330_F24_Mandar_Ambulkar/OpenCv-Workshop/lab_2_image.jpg", img)
cv2.imwrite("CS5330_F24_Mandar_Ambulkar/OpenCv-Workshop/lab_2_gray_image.jpg", gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()