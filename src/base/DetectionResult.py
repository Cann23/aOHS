class DetectionResult(object):
    """Represents the result of a detection. It is a base class for more concrete result classes (e.g HelmetDetectionResult)."""

    def __init__(self, camera):
        self.camera = camera

