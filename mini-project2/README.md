# WebCam Video Processing Script

This project implements various real-time video processing functions using OpenCV, allowing users to toggle between different features such as cropping, resizing, blurring, and more, all through keyboard inputs.

## Features
The script includes the following functionalities:
1. **Video Capture**: Opens the default webcam or a video file for live stream processing.
2. **Crop Video (`c` or `C`)**: Crops a specific region of the video.
3. **Resize Video (`r` or `R`)**: Resizes the video to a fixed dimension (320x240).
4. **Blur Video (`b` or `B`)**: Applies a Gaussian blur to the video.
5. **Add Box (`a` or `A`)**: Draws a rectangle on the video.
6. **Add Text (`t` or `T`)**: Overlays custom text (your name) on the video.
7. **Thresholding (`g` or `G`)**: Converts the video to grayscale and applies binary thresholding.
8. **Custom Function (`n` or `N`)**: Applies an additional custom effect, such as inverting colors.
9. **Quit ('q' or Q')**: Quits the webcam.