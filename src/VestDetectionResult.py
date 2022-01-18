import base.DetectionResult as DetectionResult

class VestDetectionResult(DetectionResult.DetectionResult):

    def __init__(self, camera, rect, isWearingVest):
        base.__init__(camera, rect)
        self.isWearingVest = isWearingVest

