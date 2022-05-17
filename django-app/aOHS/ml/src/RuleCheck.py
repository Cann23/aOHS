# Utilizes visitor pattern.
class RuleCheck(object):
    """Main class that performs rule checks. Tests the detections according to the rules of the zone they are in."""

    # Visit helmet detection.
    def VisitHelmet(helmetDetectionResult):
        raise NotImplementedError

    # Visit vest detection.
    def VisitVest(vestDetectionResult):
        raise NotImplementedError

    # Visit mask detection.
    def VisitMask(maskDetectionResult):
        raise NotImplementedError
