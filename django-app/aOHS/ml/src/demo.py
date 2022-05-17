import os
import sys
from time import sleep

import cv2

from OpenCVCamera import *
# Add lib folder to sys path.
p = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(p, "../lib/Helmet-Vest-Worker")
p = os.path.abspath(p)
sys.path.append(p)
cam = OpenCVCamera(0, None)

img_path = "./capture0.jpg"
while True:
    frame = cam.lastFrame
    sleep(0.1)
    if frame is not None:
        # TODO test this part
        TaskJob(frame)

        # detector.Detect(cam)
        # cv.imwrite(img_path, frame)
        result, frame = cv2.imencode('.jpg', frame, None)


