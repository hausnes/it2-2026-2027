# Source: https://pypi.org/project/opencv-python/
# Install: pip install opencv-python

import cv2

# Initialize the camera
cam = cv2.VideoCapture(0)

# Read input from the camera
result, image = cam.read()

# If input image is detected without any error, show and save the image
if result:
    cv2.imshow("Webcam Image", image)
    cv2.imwrite("webcam_image.png", image)
else:
    print("No image detected. Please try again.")

# Release the camera and close the window
cv2.waitKey(0)
cv2.destroyWindow("Webcam Image")
cam.release()