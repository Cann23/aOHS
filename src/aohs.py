import sys
import os
import cv2 as cv
from OpenCVCamera import *

# Add lib folder to sys path.
p = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(p, "../lib/Helmet-Vest-Worker")
p = os.path.abspath(p)
sys.path.append(p)

import helmetvestworker

class aOHS(object):
    """Main program class."""


cam = OpenCVCamera(-1,None)

print(type(cam.lastFrame))
cv.imshow("frame", cam.lastFrame)
cv.waitKey(0)

