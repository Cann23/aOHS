import sys
import os
from OpenCVCamera import *
from Scheduler import *

# Add lib folder to sys path.
p = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(p, "../lib/Helmet-Vest-Worker")
p = os.path.abspath(p)
sys.path.append(p)

class aOHS(object):
    """Main program class."""

    def __init__(self):
        self.scheduler = Scheduler()
        self.cameras = None

    # Creates and / or deletes cameras.
    def UpdateCameras(self):
        raise NotImplementedError
