class Scheduler(object):
    """Schedules and preferably pipelines the violation detectors."""

    # Collection of violation detectors.
    detectors
    # List of cameras.
    cameras

    # Detects the violations for given cameras, then returns detection results.
    def DetectViolations(camera):
        raise NotImplementedError
