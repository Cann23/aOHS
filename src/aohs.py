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
