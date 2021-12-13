import sys

import cv2

import main

main.prepare_model(approach=1)

img = cv2.imread(f'frames/1.jpg')
letter_boxed_img = main.letterbox_image(img, main.input_shape)
detection, is_violation_occurred = main.get_detection(letter_boxed_img, int(sys.argv[1]))

print(f"Model called for {sys.argv[0]} {sys.argv[1]} {sys.argv[2]} and violation: {is_violation_occurred}")

# main.plt_imshow(detection[:, :, ::-1])

# print(f"Model called for {sys.argv[0]} {sys.argv[1]} {sys.argv[2]}.")
