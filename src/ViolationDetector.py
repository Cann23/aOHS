class ViolationDetector(object):
    """Base class for concrete violation detectors."""

    # Takes an image and a list of zones, then performs the necessary detections and returns the detection results.
    # Child classes must override this method.
    def Detect(image, zones):
        raise NotImplementedError
