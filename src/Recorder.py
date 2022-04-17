import threading
import time
import cv2 as cv

import base.Camera as Camera


class Recorder(object):
    """Records the capture as a video format file."""

    # Initializer for a recorder object.
    # camera: Camera to record from.
    # fps: Frames per second.
    # max_duration: How long will this instance keep a recording window.
    def __init__(self, camera: Camera.Camera, fps: int, max_duration: float):
        self.camera = camera
        self.max_duration = max_duration
        self.fps = fps
        self.is_recording = False
        self.frames = []
        self.__record_job__ = None

    # Save the current data as a video file.
    # path: Path to save the file.
    # delay: How long to wait before saving the file.
    def Save(self, path, delay):
        __save_job__ = threading.Thread(target=self.__SaveJob__, args=(self, path, delay))
        __save_job__.start()

    # Starts recording.
    def StartRecording(self):
        if self.is_recording:
            return
        self.is_recording = True
        self.__record_job__ = threading.Thread(target=self.__RecordJob__, args=(self,), daemon=True)
        self.__record_job__.start()

    # Stops recording.
    def StopRecording(self):
        if self.is_recording and self.__record_job__:
            self.is_recording = False
            self.__record_job__.join()

    # Performs the recording
    def __RecordJob__(self):
        while self.is_recording:
            frame = self.camera.lastFrame
            # Add frame to the list.
            self.frames.append(frame)
            # If the frame is filled, drop until it fits the buffer.
            while len(self.frames) > self.fps * self.max_duration:
                self.frames.pop(0)

    # Performs the video saving.
    def __SaveJob__(self, path, delay):
        # Delay saving if requested.
        if delay > 0:
            time.sleep(delay)
        # Begin writing.
        writer = cv.VideoWriter(path, cv.VideoWriter_fourcc(*'MJPG'), self.fps, self.camera.size)
        for frame in self.frames:
            writer.write(frame)
        # Finish writing.
        writer.release()
