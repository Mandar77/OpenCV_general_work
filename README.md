# CS 5330: Pattern Recognition and Computer Vision

This repository contains a collection of projects and assignments for the CS 5330 course at Northeastern University. The work covers a range of topics in computer vision, from basic image manipulation to real-time video processing and deep learning applications.

## Projects Overview

### 1. OpenCV Workshop
This series of labs provides a hands-on introduction to fundamental computer vision techniques using the OpenCV library. Each lab focuses on a specific topic, building a strong foundation in image processing.

**Key Files:**
- [Lab 2: Image Loading/Saving](./OpenCv-Workshop/lab2.py)
- [Lab 3: Basic Image Operations](./OpenCv-Workshop/lab3.py)
- [Lab 4: Feature Detection](./OpenCv-Workshop/lab4.py)
- [Lab 5: Histograms](./OpenCv-Workshop/lab5.py)
- [Lab 6: Smoothing and Blurring](./OpenCv-Workshop/lab6.py)
- [Lab 8: Edge Detection](./OpenCv-Workshop/lab8.py)
- [Lab 9: Contours](./OpenCv-Workshop/lab9.py)
- [Lab 10: Optical Flow](./OpenCv-Workshop/lab10.py)
- [Lab 11: Adversarial Images & GANs](./OpenCv-Workshop/lab11.py)

### 2. Mini-Project 1: Basic Image Manipulation
This project focuses on pixel-level image manipulation using a simplified image processing library. The scripts demonstrate fundamental operations like color filtering, creating a "redscreen" (chroma key) effect, and applying filters.

**Key Files:**
- [`greenscreen.py`](./mini-project1/greenscreen.py): Replaces red pixels in an image with a background image.
- [`imageexamples.py`](./mini-project1/imageexamples.py): A collection of functions for tasks like grayscaling and darkening images.

### 3. Mini-Project 2: Real-Time and Static Image Processing with OpenCV
This project contains two parts that showcase a broader range of OpenCV capabilities.

- **Real-Time Video Processing**: An interactive script that captures a webcam feed and allows the user to apply various effects (blur, crop, threshold, etc.) in real-time using keyboard commands.
  - **File:** [`WebCam.py`](./mini-project2/WebCam.py)

- **Static Image Operations**: A script that performs a sequence of over 10 different image processing tasks on a single image, including drawing, edge detection, and contour analysis.
  - **File:** [`Assignment2-1.py`](./mini-project2/Assignment2-1.py)

### 4. Extra Credit: Real-Time Image Classification with MobileNetV2
This advanced project demonstrates the integration of a pre-trained deep learning model for a practical computer vision task. The script captures a video stream and performs real-time image classification, displaying the top predictions on the video feed.

**Key Files:**
- [`WebCamSave.py`](./extra-credit/WebCamSave.py): Implements real-time classification using the MobileNetV2 model and saves the output video.
- [`Project Description`](./extra-credit/CS5330-Mini-Project-MobileNet-Image-Classification-Fall2024.docx): The assignment document for this task.
