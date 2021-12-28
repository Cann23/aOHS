import base.HelmetVestWorkerViolationDetector as b
import base.Camera as cam
from OpenCVImageAdapter import *

class HelmetViolationDetector(b.HelmetVestWorkerViolationDetector):
    """Detects helmet violations."""

    def __init__(self):
        super.__init__(self)
        self.__violation_type__ = 1

    def Detect(camera: cam.Camera):
        adapter = OpenCVImageAdapter()
        img = adapter.GetImage(camera)
        detection, has_violation_occured = self.GetDetection(img, self.__violation_type__)
        raise NotImplementedError
