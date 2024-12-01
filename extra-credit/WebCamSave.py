import os
import cv2
import numpy as np
import argparse
import tensorflow as tf

# Set up argument parser
parser = argparse.ArgumentParser(description="Video file path or camera input")
parser.add_argument("-f", "--file", type=str, help="Path to the video file")
args = parser.parse_args()

# Load pre-trained MobileNet model
model = tf.keras.applications.MobileNetV2(weights='imagenet')

# Initialize video capture
if args.file:
    cap = cv2.VideoCapture(args.file)
else:
    cap = cv2.VideoCapture(0)  # Use default camera

# Get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Initialize video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess the frame for MobileNet
    input_frame = cv2.resize(frame, (224, 224))
    input_frame = tf.keras.applications.mobilenet_v2.preprocess_input(input_frame)
    input_frame = np.expand_dims(input_frame, axis=0)

    # Perform classification
    predictions = model.predict(input_frame)
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=3)[0]

    # Draw predictions on the frame
    for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
        cv2.putText(frame, f"{label}: {score:.2f}", (10, 30 + i * 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('MobileNet Classification', frame)

    # Write frame to output video
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()