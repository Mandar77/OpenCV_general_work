# Extra Credit: Real-Time Image Classification with MobileNetV2

This project demonstrates an advanced computer vision application by implementing a real-time image classification system. It uses a pre-trained deep learning model to classify objects in a live video stream from a webcam or a video file.

## `WebCamSave.py`

This script is the core of the project. It performs the following steps:
1.  **Initializes Video Capture**: Opens a video stream from either a connected webcam or a specified video file path using an argument parser.
2.  **Loads Pre-trained Model**: Loads the **MobileNetV2** model with weights pre-trained on the ImageNet dataset, provided by TensorFlow/Keras.
3.  **Processes Frames**: In a loop, it reads frames from the video stream. Each frame is:
    - Resized to 224x224 pixels, the required input size for MobileNetV2.
    - Preprocessed to match the model's expected input format.
4.  **Performs Classification**: The processed frame is passed to the MobileNetV2 model, which returns a set of predictions.
5.  **Displays Results**: The top 3 predictions (with their labels and confidence scores) are decoded and overlaid onto the original video frame.
6.  **Saves Output**: The resulting video, including the classification text, is displayed on the screen and simultaneously saved to an output file named `output.avi`.
7.  **Quits**: The application can be closed by pressing the `q` key.

### Dependencies
- OpenCV (`cv2`)
- TensorFlow (`tf.keras`)
- NumPy

### How to Run
You can run the script with a webcam or provide a path to a video file.

**Using webcam:**
```bash
python WebCamSave.py
```

**Using a video file:**
```bash
python WebCamSave.py --file path/to/your/video.mp4
```
