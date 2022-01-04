import threading
import cv2 as cv

import base.Camera as Camera

class OpenCVCamera(Camera.Camera):
    """OpenCV Implementation of Camera."""

    def __init__(self, id, rules):
        super().__init__(id, rules)
        self.__videoCapture__ = None
        self.isCapturing = False
        self.Activate()

    def __capture__(self):
        while self.isCapturing:
            # Make sure the capture handle is active and working.
            if self.__videoCapture__ is None or not self.__videoCapture__.isOpened():
                # Invalid handle, try again.
                self.__videoCapture__ = cv.VideoCapture(self.id)
                if self.__videoCapture__ and self.__videoCapture__.isOpened():
                    width = int(self.__videoCapture__.get(3))
                    height = int(self.__videoCapture__.get(4))
                    self.size = (width, height)
            else:
                ret, frame = self.__videoCapture__.read()
                self.lastFrame = frame

    # Starts capturing.
    def Activate(self):
        if self.isCapturing:
            # Already capturing.
            return
        self.isCapturing = True
        self.__capture_job__ = threading.Thread(target=self.__capture__)
        self.__capture_job__.start()

    # Releases the camera capture.
    def Release(self):
        if not self.isCapturing:
            # Already inactive.
            return
        self.isCapturing = False
        if self.__capture_job__ is not None:
            self.__capture_job__.join()
            self.__capture_job__ = None
            self.__videoCapture__ = None
