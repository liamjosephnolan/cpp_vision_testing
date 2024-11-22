import cv2
import numpy as np

# Load the image
image = cv2.imread('high_rez.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = cv2.equalizeHist(gray)

gray = cv2.GaussianBlur(gray, (5, 5), 0)

alpha = .5 # Contrast control
gray = cv2.convertScaleAbs(gray, alpha=alpha)

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters()

# Create the ArUco detector
detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)
# Detect the markers
corners, ids, rejected = detector.detectMarkers(gray)
# Print the detected markers

cv2.imshow('Test image',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("Detected markers:", ids)
if ids is not None:
    cv2.aruco.drawDetectedMarkers(image, corners, ids)
    cv2.imshow('Detected Markers', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
