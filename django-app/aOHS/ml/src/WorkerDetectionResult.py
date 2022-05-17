import base.DetectionResult as DetectionResult

class WorkerDetectionResult(DetectionResult.DetectionResult):

    def __init__(self, camera, rect, doesExist):
        super.__init__(camera, rect)
        self.doesExist = doesExist

