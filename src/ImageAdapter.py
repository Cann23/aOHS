class ImageAdapter(object):
    """Adapter for system's image input. Live and offline videos, as well as images could be adapted to the system."""

    # Gets the current capture of a camera, and returns in the system acceptable format.
    def GetImage(camera):
        raise NotImplementedError
