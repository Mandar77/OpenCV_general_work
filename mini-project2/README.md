# Mini-Project 2: Image and Video Processing with OpenCV

This directory contains two separate assignments that demonstrate a range of image and video processing capabilities using the OpenCV library.

---

## 1. `WebCam.py`: Real-Time Video Processing

This script captures video from a webcam and allows for various effects to be applied to the live feed in real-time. The effects are toggled on and off using keyboard commands.

### Features & Controls
- **Crop Video**: Toggled with `c` or `C`. Crops the video to a predefined region.
- **Resize Video**: Toggled with `r` or `R`. Resizes the video frame to 320x240 pixels.
- **Blur Video**: Toggled with `b` or `B`. Applies a Gaussian blur to the entire frame.
- **Add Box**: Toggled with `a` or `A`. Draws a static green rectangle on the video.
- **Add Text**: Toggled with `t` or `T`. Overlays a name on the top-left of the video.
- **Grayscale Thresholding**: Toggled with `g` or `G`. Converts the video to grayscale and applies a binary threshold.
- **Invert Colors**: Toggled with `n` or `N`. A custom function that inverts the colors of the video frame.
- **Quit**: Press `q` or `Q` to close the video feed and terminate the script.

---

## 2. `Assignment2-1.py`: Static Image Manipulation

This script is a comprehensive demonstration of fundamental image processing operations applied sequentially to a single static image (`flower.png`). It serves as a showcase of core OpenCV functionalities.

### Operations Performed
The script applies the following transformations in order:
1.  **Region of Interest (ROI)**: Extracts and displays a specific rectangular section of the image.
2.  **Resizing**: Scales the image down to 200x200 pixels.
3.  **Rotation**: Rotates the image 45 degrees clockwise.
4.  **Smoothing**: Applies a Gaussian blur to the image.
5.  **Drawing Shapes**: Adds a rectangle, a circle, and a line to the image.
6.  **Adding Text**: Overlays a name on the image.
7.  **Grayscale Conversion**: Converts the image to grayscale.
8.  **Edge Detection**: Applies the Canny edge detector.
9.  **Thresholding**: Applies a binary threshold to the grayscale image.
10. **Contour Detection**: Finds and draws the contours of the objects in the thresholded image.

The final image with contours is saved as `flower_copy.png`.
