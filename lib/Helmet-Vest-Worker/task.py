import sqlite3
import subprocess
import threading
from datetime import time
from time import sleep

import model_caller

connection = sqlite3.connect('../../django-app/aOHS/db.sqlite3')
cur_cursor = connection.cursor()

sql_get_config = "select c.id, m.id, m.path, co.id, co.violationCounter,c.url " \
                 "from backend_camera c " \
                 "join backend_configuration co on co.cameraId_id = c.id " \
                 "join backend_model m on m.id = co.modelId_id " \
                 "where c.active = 1 "


#
# def executeModel(camera_id, model_id, model_path):
#     command_str = f"python ./model_caller.py {camera_id} {model_id} {model_path} " + time().strftime("%m/%d%Y %H:%M:%S")
#     output = subprocess.check_output([command_str], shell=True)
#     print(output.decode("utf-8"))


def TaskJob():
    while True:

        cur_cursor.execute(sql_get_config)
        result_set = cur_cursor.fetchall()

        thread_list = []
        for conf in result_set:
            curr_thread = threading.Thread(target=model_caller.model_caller, args=(conf,))
            thread_list.append(curr_thread)

            curr_thread.start()

        for th in thread_list:
            th.join()

        print("One cycle done.")


TaskJob()
