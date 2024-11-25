import time 
import cv2
import numpy as np


marker_size = 0.1 # meters
focal_length = 500 # Pixels
# Initialize the webcam
cap = cv2.VideoCapture(0)  # 0 is the default webcam, change if you have multiple cameras

# Check if the webcam is accessible
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Load the ArUco dictionary and set parameters
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_7X7_250)
parameters = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)

print("Press 'q' to quit.")

while True:

    # Capture a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect the markers
    corners, ids, rejected = detector.detectMarkers(gray)
    

    print(ids)
    # Draw detected markers on the frame
    if ids is not None:
        for marker_corners in corners:
            # marker_corners has shape (1, 4, 2)
            corners_2d = marker_corners[0]  # Extract the (4, 2) array

            # Upper-left corner
            upper_left = tuple(corners_2d[0])

            # Upper-right corner
            upper_right = tuple(corners_2d[1])
        pixel_distance = np.sqrt((upper_right[1] - upper_left[0])**2 + (upper_right[0]- upper_left[1])**2)
        distance_m = (marker_size * focal_length) / pixel_distance
        print(upper_left)
        print(upper_right)
        print(pixel_distance)
        print(f"Estimated distance to the marker: {distance_m} meters")

        cv2.aruco.drawDetectedMarkers(frame, corners, ids)
        cv2.imshow('Detected Markers', frame)
    else:
    # Show the frame with detected markers
        cv2.imshow('Detected Markers', gray)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()

