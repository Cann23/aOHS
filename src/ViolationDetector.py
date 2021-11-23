class ViolationDetector(object):
    """Base class for concrete violation detectors."""

    # Takes a camera, then performs the necessary detections and returns the detection results.
    # Child classes must override this method.
    def Detect(camera):
        raise NotImplementedError
