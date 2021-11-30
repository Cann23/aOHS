import cv2
from .models import Camera


def capture_camera(camera_id):
    # queries the camera from database by id
    camera = Camera.objects.get(id=camera_id)

    # gets rtsp link of the camera from this object
    video = cv2.VideoCapture(camera.url)

    # starts video capturing process using opencv
    while camera.active:
        _, frame = video.read()
        cv2.imshow("RTSP", frame) # for now just show image in the screen since we do not decided how to save files yet.
        # save the captures to the database

    video.release()
    cv2.destroyWindow("RTSP")
