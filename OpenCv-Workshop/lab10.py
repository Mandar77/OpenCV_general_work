# implementation 1

# import cv2
# import numpy as np

# # Set up camera
# cap = cv2.VideoCapture(0)

# # Parameters for Shi-Tomasi Corner Detection to find points for Lucas-Kanade
# feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)

# # Parameters for Lucas-Kanade Optical Flow
# lk_params = dict(winSize=(15, 15), maxLevel=2, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# # Read the first frame
# ret, old_frame = cap.read()
# if not ret:
#     print("Failed to capture initial frame.")
#     cap.release()
#     exit()

# old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
# p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)
# mask = np.zeros_like(old_frame)

# frame_count = 0  # To save frames for checking

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

#     if p1 is not None:
#         good_new = p1[st == 1]
#         good_old = p0[st == 1]

#         for i, (new, old) in enumerate(zip(good_new, good_old)):
#             a, b = int(new[0]), int(new[1])
#             c, d = int(old[0]), int(old[1])
#             mask = cv2.line(mask, (a, b), (c, d), (0, 255, 0), 2)
#             frame = cv2.circle(frame, (a, b), 5, (0, 0, 255), -1)

#         lk_output = cv2.add(frame, mask)

#     # Saving frames instead of using cv2.imshow for testing
#     cv2.imwrite(f"lab10_results/output_frame_{frame_count}.png", lk_output)
#     frame_count += 1

#     old_gray = frame_gray.copy()
#     if p1 is not None:
#         p0 = good_new.reshape(-1, 1, 2)

#     if frame_count > 100:  # Limit the saved frames for storage control
#         break

# cap.release()

#implementation 2
import cv2
import numpy as np

# Set up camera
cap = cv2.VideoCapture(0)

# Parameters for Shi-Tomasi Corner Detection to find points for Lucas-Kanade
feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)

# Parameters for Lucas-Kanade Optical Flow
lk_params = dict(winSize=(15, 15), maxLevel=2, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Read the first frame
ret, old_frame = cap.read()
if not ret:
    print("Failed to capture initial frame.")
    cap.release()
    exit()

old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)
mask = np.zeros_like(old_frame)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

    if p1 is not None:
        good_new = p1[st == 1]
        good_old = p0[st == 1]

        for i, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = int(new[0]), int(new[1])
            c, d = int(old[0]), int(old[1])
            mask = cv2.line(mask, (a, b), (c, d), (0, 255, 0), 2)
            frame = cv2.circle(frame, (a, b), 5, (0, 0, 255), -1)

        lk_output = cv2.add(frame, mask)
    else:
        lk_output = frame

    # Display the result live
    cv2.imshow("Lucas-Kanade Optical Flow (Sparse)", lk_output)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    old_gray = frame_gray.copy()
    if p1 is not None:
        p0 = good_new.reshape(-1, 1, 2)

cap.release()
cv2.destroyAllWindows()
