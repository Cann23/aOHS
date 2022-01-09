import sys
import os
import cv2 as cv
from OpenCVCamera import *
#from HelmetViolationDetector import *
from time import sleep

# Add lib folder to sys path.
p = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(p, "../lib/Helmet-Vest-Worker")
p = os.path.abspath(p)
sys.path.append(p)
# 'http://192.168.1.102:8080/video'
# Open the first camera.
cam = OpenCVCamera(0, None)
#detector = HelmetViolationDetector()
# Save the frame to an image.
img_path = "./capture0.jpg"
while True:
    frame = cam.lastFrame
    sleep(0.1)
    if frame is not None:
    	#detector.Detect(cam)
    	cv.imwrite(img_path, frame)

