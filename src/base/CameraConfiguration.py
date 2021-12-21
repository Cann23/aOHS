class CameraConfiguration(object):
    """Handles the configuration tasks to set rules for cameras."""

    # Gets the rules for the given camera, raises an error if the camera does not exist.
    def GetRules(camera):
        raise NotImplementedError

    # Sets the given rules for the given camera, raises an error if the camera does not exist.
    def SetRules(camera, rules):
        raise NotImplementedError
