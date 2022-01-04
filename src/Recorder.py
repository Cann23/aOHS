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
        self._record_job_ = None

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
        _record_job_ = threading.Thread(target=self.__RecordJob__)
        _record_job_.start()

    # Stops recording.
    def StopRecording(self):
        if is_recording and _record_job_:
            is_recording = False
            _record_job_.join()

    # Performs the recording
    def __RecordJob__(self):
        while is_recording:
            frame = self.camera.lastFrame
            # Add frame to the list.
            self.frames.append(frame)
            # If the frame is filled, drop until it fits the buffer.
            while frames.length() > fps * max_duration:
                frames.pop(0)

    
