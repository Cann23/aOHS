import sys
import os
import cv2 as cv
from OpenCVCamera import *

# Add lib folder to sys path.
p = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(p, "../lib/Helmet-Vest-Worker")
p = os.path.abspath(p)
sys.path.append(p)

#import helmetvestworker

class aOHS(object):
    """Main program class."""


cam = OpenCVCamera(0, None)

print(cam.lastFrame)
while True:
    if cam.lastFrame is not None:
        cv.imshow("img", cam.lastFrame)
        cv.waitKey(0)
        cam.isCapturing = False
        break


