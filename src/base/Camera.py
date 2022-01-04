class Camera(object):
    """Represents a camera, for which the associated rules will be checked against."""

    # Constructor where all attributes are assigned.
    def __init__(self, id, rules):
        # Identifier for the camera.
        # -1: Invalid.
        # Non-negative: Unique id.
        self.id = id
        # Rules for the camera.
        self.rules = rules
        # Latest capture of this camera.
        self.lastFrame = None
        # Frame size in pixels: (width, height).
        self.size = (0, 0)
