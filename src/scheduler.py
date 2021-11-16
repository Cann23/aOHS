class Scheduler(object):
    """Schedules and preferably pipelines the violation detectors."""

    # Collection of violation detectors.
    detectors
    # List of zones.
    zones

    # Detects the violations given image and zones, then returns detection results.
    def DetectViolations(image, zones):
        raise NotImplementedError
