# OpenCV Workshops

This directory contains a series of workshop assignments from the CS 5330: Pattern Recognition and Computer Vision course. These labs cover fundamental to advanced techniques in image processing and computer vision using Python with the OpenCV and PyTorch libraries.

## Workshop Details

### [lab2.py](./lab2.py) - Loading, Displaying, and Saving Images
This script covers the most basic file operations in OpenCV. It demonstrates how to:
- Load an image from a file in both full color and grayscale using `cv2.imread()`.
- Display images in a window on the screen using `cv2.imshow()`.
- Save the loaded images back to disk using `cv2.imwrite()`.

### [lab3.py](./lab3.py) - Basic Image Operations
This lab explores common image transformations and modifications. The script shows how to:
- Resize an image to a specific dimension.
- Add text overlays onto an image.
- Convert an image between different color spaces (e.g., BGR to Grayscale and BGR to HSV).

### [lab4.py](./lab4.py) - Feature Detection
This script introduces feature detection, a critical component of many computer vision tasks. It implements two popular methods:
- **Harris Corner Detection**: Identifies corners in an image.
- **SIFT (Scale-Invariant Feature Transform)**: Detects and computes keypoints and their descriptors.

### [lab5.py](./lab5.py) - Image Histograms
This lab focuses on creating and visualizing image histograms to understand pixel intensity distribution. The script generates:
- A 1D grayscale histogram.
- A 1D color histogram (for B, G, and R channels).
- A 2D color histogram (for Blue and Green channels).

### [lab6.py](./lab6.py) - Smoothing and Blurring
This script demonstrates various techniques for image smoothing, which is often used to reduce noise and detail. The implemented filters include:
- Averaging (Box Filter)
- Gaussian Blurring
- Median Blurring
- Bilateral Filtering

### [lab8.py](./lab8.py) - Edge Detection
This lab covers two fundamental algorithms for detecting edges in an image:
- **Sobel Edge Detection**: Uses derivatives to find edges.
- **Canny Edge Detection**: A multi-stage algorithm for robust edge detection.

### [lab9.py](./lab9.py) - Contour Analysis
This script explores how to find, analyze, and draw contours in an image. The experiments include:
- Finding contours with different retrieval modes (`RETR_LIST`, `RETR_TREE`).
- Sorting contours by area and drawing the top 5 largest.
- Drawing bounding boxes and minimum enclosing circles around detected contours.

### [lab10.py](./lab10.py) - Optical Flow
This lab moves into video analysis, demonstrating how to track motion across frames using sparse optical flow. The script:
- Uses the **Shi-Tomasi Corner Detector** to find strong corners to track.
- Implements the **Lucas-Kanade optical flow** algorithm to follow these points in a real-time webcam feed.

### [lab11.py](./lab11.py) - Advanced Topics
This script touches on more advanced concepts, including adversarial machine learning and generative models. It demonstrates how to:
- Create an "adversarial" image by adding synthetic noise.
- Define a basic **Generative Adversarial Network (GAN)** with a Generator and Discriminator using PyTorch.
- Add Gaussian noise to an image and then denoise it using a Gaussian blur.
