import sys
import os
import cv2 as cv
from OpenCVCamera import *
#from HelmetViolationDetector import *
from time import sleep
import socket
import sys
import cv2
import pickle
import numpy as np
import struct ## new
import zlib

HOST=''
PORT=8485

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST,PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')

conn,addr=s.accept()
# Add lib folder to sys path.
p = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(p, "../lib/Helmet-Vest-Worker")
p = os.path.abspath(p)
sys.path.append(p)
# 'http://192.168.1.102:8080/video'
# Open the first camera.
cam = OpenCVCamera(0, None)
# detector = HelmetViolationDetector()
# Save the frame to an image.
img_path = "./capture0.jpg"
while True:
    frame = cam.lastFrame
    sleep(0.1)
    if frame is not None:
        # detector.Detect(cam)
        # cv.imwrite(img_path, frame)
        result, frame = cv2.imencode('.jpg', frame, encode_param)
        #    data = zlib.compress(pickle.dumps(frame, 0))
        data = pickle.dumps(frame, 0)
        size = len(data)
        client_socket.sendall(struct.pack(">L", size) + data)

