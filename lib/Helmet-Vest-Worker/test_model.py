import  main
import cv2
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import time

main.prepare_model(approach=1)
f = open("input.txt", "r")
violation_type = int(f.read(1))
for i in range(12):
    # read the image
    while(not os.path.isfile(f'frames/{i}.jpg')):
        time.sleep(1)
    img = cv2.imread( f'frames/{i}.jpg' )

    # resize
    img = main.letterbox_image(img, main.input_shape)

    # get the detection on the image
    #0 = only worker
    #1 = for helmet
    #2 = for vest
    #3 = both helmet and vest
    img1 = main.get_detection(img,violation_type)
    # show the image
    main.plt_imshow(img1[:, :, ::-1])
