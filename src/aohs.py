import sys
import os
from 
from Camera import *
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
