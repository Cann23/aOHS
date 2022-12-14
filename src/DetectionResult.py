class DetectionResult(object):
    """Represents the result of a detection. It is a base class for more concrete result classes (e.g HelmetDetectionResult)."""

    # Associated camera.
    camera
    # Screen space info.
    rect

    # Accept a visitor for rule checking.
    # Child classes must override this method.
    def Accept(ruleCheck):
        raise NotImplementedError
