import aOHS

def test():
    cam = OpenCVCamera(0, None)
    print(cam.lastFrame)
    while True:
        if cam.lastFrame is not None:
            cv.imshow("img", cam.lastFrame)
            cv.waitKey(0)
            cam.isCapturing = False
            break

test()
