import datetime
import sys

import cv2

import main



def model_caller(camera_id, model_id, model_path, frame):


    main.prepare_model(approach=1)

    # img = cv2.imread(f'frames/1.jpg')
    letter_boxed_img = main.letterbox_image(img, main.input_shape)
    detection, is_violation_occurred = main.get_detection(letter_boxed_img, int(model_id))

    print(f"Model called for {camera_id} {model_id} {model_path} and violation: {is_violation_occurred}")
    img_path = f"{datetime.datetime.now()}.jpg"
    cv.imwrite(img_path, frame)

    insert_sql = f"insert into backend_Violation " \
                 "values (null, {camera_id}, null, {model_id}, null, null, false, {image_path}, null, null ) "

# main.plt_imshow(detection[:, :, ::-1])

# print(f"Model called for {sys.argv[0]} {model_id} {model_path}.")
