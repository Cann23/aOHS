import threading
import time

import base.Camera as Camera

class Recorder(object):
    """Records the capture as a video format file."""

    # Initializer for a recorder object.
    # camera: Camera to record from.
    # fps: Frames per second.
    # max_duration: How long will this instance keep a recording window.
    def __init__(self, camera : Camera.Camera, fps : int, max_duration : float):
        self.camera = camera
        self.max_duration = max_duration
        self.is_recording = False
        self.frames = []
        self.__record_job__ = None

    # Save the current data as a video file.
    # path: Path to save the file.
    # delay: How long to wait before saving the file.
    def Save(self, path, delay):
        pass

    # Starts recording.
    def StartRecording(self):
        if is_recording:
            return
        is_recording = True
        self.__record_job__ = threading.Thread(target=self.__RecordJob__)
        self.__record_job__.start()

    # Stops recording.
    def StopRecording(self):
        if is_recording and __record_job__:
            is_recording = False
            self.__record_job__.join()

    # Performs the recording
    def __RecordJob__(self):
        while is_recording:
            frame = self.camera.lastFrame
            # Add frame to the list.
            self.frames.append(frame)
            # If the frame is filled, drop until it fits the buffer.
            while frames.length() > fps * max_duration:
                frames.pop(0)

    
