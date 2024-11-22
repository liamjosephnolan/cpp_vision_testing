import time 
import cv2
import numpy as np

# Initialize the webcam
cap = cv2.VideoCapture(0)  # 0 is the default webcam, change if you have multiple cameras

# Check if the webcam is accessible
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Load the ArUco dictionary and set parameters
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)

print("Press 'q' to quit.")

while True:
    time.sleep(.25)

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
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)

    # Show the frame with detected markers
    cv2.imshow('Detected Markers', gray)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()

