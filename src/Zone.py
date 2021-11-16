class Zone(object):
    """Represents a zone, for which the associated rules will be checked against."""

    # Identifier for the zone.
    # -1: Invalid.
    # Non-negative: Unique id.
    id = -1
    # Current rectangle for the zone in screen space.
    rect
    # Rules for the zone.
    rules

    # Constructor where all attributes are assigned.
    def __init__(self, id, rect, rules):
        self.id = id
        self.rect = rect
        self.rules = rules
