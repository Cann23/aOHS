import sys
import os
import cv2 as cv
from OpenCVCamera import *

# Add lib folder to sys path.
p = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(p, "../lib/Helmet-Vest-Worker")
p = os.path.abspath(p)
sys.path.append(p)

# Open the first camera.
cam = OpenCVCamera(0, None)
# Save the frame to an image.
img_path = "./capture0.jpg"
while True:
    frame = cam.lastFrame
    cv.imwrite(img_path, frame)
