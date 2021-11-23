class Camera(object):
    """Represents a camera, for which the associated rules will be checked against."""

    # Identifier for the camera.
    # -1: Invalid.
    # Non-negative: Unique id.
    id = -1
    # Rules for the camera.
    rules
    # Latest capture of this camera.
    latestCapture

    # Constructor where all attributes are assigned.
    def __init__(self, id, rules):
        self.id = id
        self.rules = rules
