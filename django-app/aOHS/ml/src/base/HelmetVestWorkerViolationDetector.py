import helmetvestworker as model
from ViolationDetector import *

class HelmetVestWorkerViolationDetector(ViolationDetector):
    """Base violation detector class for helmet, vest and worker types since they share a single ml model"""

    __has_prepared_model__ = False

    def __init__(self):
        super.__init__(self)
        if (not __has_prepared_model__):
            model.prepare_model(1)
            __has_prepared_model__ = True

    def GetDetection(self, img, violation_type):
        return model.get_detection(img, violation_type)
