class Recorder(object):
    """Records the capture as a video format file."""

    # Initializer for a recorder object.
    # device: Device to record from.
    # max_duration: How long will this instance keep a recording window.
    def __init__(self, device, max_duration):
        this.device = device
        this.max_duration = max_duration
        this.is_recording = false

    # Save the current data as a video file.
    # path: Path to save the file.
    # delay: How long to wait before saving the file.
    def Save(path, delay):
        raise NotImplementedError

    # Starts recording.
    def StartRecording():
        raise NotImplementedError

    # Stops recording.
    def StopRecording():
        raise NotImplementedError