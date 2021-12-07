import threading
import time
import numpy
import cv2

class Recorder(object):
    """Records the capture as a video format file."""

    # Initializer for a recorder object.
    # device: Device to record from.
    # fps: Frames per second.
    # max_duration: How long will this instance keep a recording window.
    def __init__(self, device, fps, max_duration):
        this.device = device
        this.max_duration = max_duration
        this.is_recording = False
        this.frames = []
        this._record_job_ = None

    # Save the current data as a video file.
    # path: Path to save the file.
    # delay: How long to wait before saving the file.
    def Save(self, path, delay):
        raise NotImplementedError

    # Starts recording.
    def StartRecording(self):
        if is_recording:
            return
        is_recording = True
        _record_job_ = threading.Thread(target=Record_Job, args=(self,))
        _record_job_.start()

    # Stops recording.
    def StopRecording(self):
        if is_recording and _record_job_:
            is_recording = False
            _record_job_.join()

    # Performs the recording
    def Record_Job(self):
        while is_recording:
            # Begin capture.
            cap = cv.VideoCapture(device)
            if cap.isOpened():
                ret, frame = cap.read()
                # Cannot receive frame from camera?
                if not ret:
                    break
                # Add frame to the list.
                frames.append(frame)
                # If the frame is filled, drop the first frame.
                if frames.length() > fps * max_duration:
                    frames.pop(0)
        # Recording has stopped, release the capture.
        if cap:
            cap.release()
