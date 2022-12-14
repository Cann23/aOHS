import datetime
import sqlite3
import sys
from time import sleep

import cv2 as cv

import main

set_violation_counter = "update backend_configuration " \
                        "set violationCounter = ? " \
                        "where id = ? "


def model_caller(conf):
    camera_id = conf[0]
    model_id = conf[1]
    model_path = conf[2]
    configuration_id = conf[3]
    violation_counter = conf[4]
    main.prepare_model(approach=1)
    cap = cv.VideoCapture(conf[5])
    if not cap.isOpened():

        print("Cannot open camera with id: " + str(camera_id))
        sys.exit()
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        letter_boxed_img = main.letterbox_image(frame, main.input_shape)
        detection, is_violation_occurred = main.get_detection(letter_boxed_img, int(model_id)-1)

        if is_violation_occurred:
            print("camera id: " + str(camera_id) + " detected violation")
            if violation_counter >= 5:
                violation_counter = 0
                date = datetime.datetime.now()
                print(date)
                imgName = "violations/" + str(date).replace(":","_") + ".jpg"
                imgPath = "../../django-app/aOHS/static/images/" + imgName
                cv.imwrite(imgPath, detection)
                print(f"Model called for {camera_id} {model_id} {model_path} and violation: {is_violation_occurred}")
                insert_sql = f"insert into backend_violation  (cameraId_id ,modelId_id,valid,capture, created,modified,isNotified)" \
                             f"values ( {camera_id}, {model_id}, true, '{imgName}','{date}' ,'{date}' ,false) "

                print(insert_sql)
                try:
                    connection = sqlite3.connect('../../django-app/aOHS/db.sqlite3')
                    cur_cursor = connection.cursor()
                    cur_cursor.execute(insert_sql)
                    cur_cursor.execute(set_violation_counter, (violation_counter, configuration_id,))
                    connection.commit()
                    connection.close()
                except Exception as e:
                    print(e)
            else:
                violation_counter += 1
                try:
                    connection = sqlite3.connect('../../django-app/aOHS/db.sqlite3')
                    cur_cursor = connection.cursor()
                    cur_cursor.execute(set_violation_counter, (violation_counter, configuration_id,))
                    connection.commit()
                    connection.close()
                except Exception as e:
                    print(e)

            sleep(5)

        # cv.imshow('frame', detection)
        # if cv.waitKey(1) & 0xFF == ord('q'):
        #     break

    # img = cv.imread(f'./1.jpg')

    # img_path = f"{datetime.datetime.now()}.jpg"
    #  cv.imwrite(img_path, frame)

    print(f"Model called for {sys.argv[0]} {model_id} {model_path}.")

# main.plt_imshow(detection[:, :, ::-1])
