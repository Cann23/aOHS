import base.HelmetVestWorkerViolationDetector as b
import base.Camera as cam
from OpenCVImageAdapter import *

class WorkerViolationDetector(b.HelmetVestWorkerViolationDetector):
    """Detects worker violations."""

    def __init__(self):
        super.__init__(self)
        self.__violation_type__ = 0

    def Detect(self, camera: cam.Camera):
        adapter = OpenCVImageAdapter()
        img = adapter.GetImage(camera)
        detection, has_violation_occured = self.GetDetection(img, self.__violation_type__)
        raise NotImplementedError
