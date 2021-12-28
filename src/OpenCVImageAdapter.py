import base.ImageAdapter as ia
import base.Camera as cam

class OpenCVImageAdapter(ia.ImageAdapter):
    """Image adapter for ml that takes frames from openCV camera"""

    def __init__(self):
        pass

    def GetImage(self, camera: cam.Camera):
        frame = camera.lastFrame
        raise NotImplementedError
