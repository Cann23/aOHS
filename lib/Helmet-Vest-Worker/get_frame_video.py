import cv2
import time
# Opens the Video file
cap= cv2.VideoCapture("http://192.168.1.102:8080/video")
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite('frames/'+str(i)+'.jpg',frame)
    i+=1
    time.sleep(0.1)

cap.release()
cv2.destroyAllWindows()
