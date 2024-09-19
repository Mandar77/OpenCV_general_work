# USAGE: python WebCam.py

import cv2
import time

# Open video file or webcam stream
vs = cv2.VideoCapture(0)  # 0 for webcam, replace with filename for a video file
time.sleep(2.0)

# Flags to toggle different features
crop_mode = False
resize_mode = False
blur_mode = False
box_mode = False
text_mode = False
threshold_mode = False
new_function_mode = False

# loop over the frames from the video stream
while True:
    # Grab the frame from the video stream
    ret, frame = vs.read()

    if not ret:
        break

    # Perform operations based on toggled flags
    if crop_mode:
        frame = frame[50:300, 100:400]  # Example crop region

    if resize_mode:
        frame = cv2.resize(frame, (320, 240))

    if blur_mode:
        frame = cv2.GaussianBlur(frame, (15, 15), 0)

    if box_mode:
        cv2.rectangle(frame, (50, 50), (200, 200), (0, 255, 0), 2)

    if text_mode:
        cv2.putText(frame, "Mandar Ambulkar", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    if threshold_mode:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, frame = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

    if new_function_mode:
        # You can implement a custom function here, for now, we'll just invert the frame
        frame = cv2.bitwise_not(frame)

    # Display the frame
    cv2.imshow("WebCam Feed", frame)
    key = cv2.waitKey(1) & 0xFF

    # Toggle features based on key press
    if key == ord("q"):
        break
    elif key == ord("c") or key == ord("C"):
        crop_mode = not crop_mode
    elif key == ord("r") or key == ord("R"):
        resize_mode = not resize_mode
    elif key == ord("b") or key == ord("B"):
        blur_mode = not blur_mode
    elif key == ord("a") or key == ord("A"):
        box_mode = not box_mode
    elif key == ord("t") or key == ord("T"):
        text_mode = not text_mode
    elif key == ord("g") or key == ord("G"):
        threshold_mode = not threshold_mode
    elif key == ord("n") or key == ord("N"):
        new_function_mode = not new_function_mode

# Cleanup
cv2.destroyAllWindows()
vs.release()
