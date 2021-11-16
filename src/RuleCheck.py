# Utilizes visitor pattern.
class RuleCheck(object):
    """Main class that performs rule checks. Tests the detections according to the rules of the zone they are in."""

    # Visit mask detection.
    def VisitMask(maskDetectionResult):
        raise NotImplementedError

    # Visit human detection.
    def VisitHuman(humanDetectionResult):
        raise NotImplementedError
