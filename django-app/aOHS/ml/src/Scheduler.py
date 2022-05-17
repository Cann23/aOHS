import threading
import time
import base.Camera as Camera

class Scheduler(object):
    """Schedules and preferably pipelines the violation detectors."""

    def __init__(self):
        # Whether it is scheduling or not.
        self.isScheduling = False
        # Collection of violation detectors.
        self.__detectors__ = []
        # Collection of cameras.
        self.__cameras__ = []
        # Schedule job.
        self.__job__ = None
        # Whether to terminate job.
        self.__terminate_job__ = False


    # Detects the violations for given cameras, then returns detection results.
    def DetectViolations(camera):
        raise NotImplementedError

    # Starts scheduling violation detection.
    def Start(self):
        if self.__job__:
            print("Scheduler has already started.")
            return
        self.__terminate_job__ = False
        self.__job__ = threading.Thread(target=self.__schedule__)
        self.__job__.start()

    # Stops scheduling violation detection.
    def Stop(self):
        if not self.__job__:
            print("Scheduler has not begun.")
            return
        self.__terminate_job__ = True
        self.__job__.join()
        self.__job__ = None

    # Resumes scheduling violation detection.
    def Resume(self):
        if not self.__job__:
            print("Scheduler has not begun.")
            return
        if not self.isScheduling:
            self.isScheduling = True
        else:
            print("Scheduler is already resumed.")

    # Pauses scheduling violation detection.
    def Pause(self):
        if not self.__job__:
            print("Scheduler has not begun.")
            return
        if self.isScheduling:
            self.isScheduling = False
        else:
            print("Scheduler is already paused.")

    def AddCamera(self, camera: Camera.Camera):
        if camera not in self.__cameras__:
            self.__cameras__.append(camera)
        else:
            print("Camera is already in the list.")

    def RemoveCamera(self, camera: Camera.Camera):
        if camera in self.__cameras__:
            self.__cameras__.remove(camera)
        else:
            print("Camera is not in the list.")

    def __schedule__(self):
        while True:
            if self.__terminate_job__:
                return
            while not self.isScheduling:
                time.sleep(0.25)
            raise NotImplementedError
