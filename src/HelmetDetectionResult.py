import base.DetectionResult as DetectionResult

class HelmetDetectionResult(DetectionResult.DetectionResult):

    def __init__(self, camera, rect, isWearingHelmet):
        base.__init__(camera, rect)
        self.isWearingHelmet = isWearingHelmet

