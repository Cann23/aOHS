import os
import sqlite3
import subprocess
import threading
from datetime import time

connection = sqlite3.connect('../django-app/aOHS/db.sqlite3')
cur_cursor = connection.cursor()

sql_get_config = "select c.id, m.id, m.path " \
                 "from backend_camera c " \
                 "join backend_configuration co on co.cameraId_id = c.id " \
                 "join backend_model m on m.id = co.modelId_id " \
                 "where c.active = 1 "


def executeModel(model_path, camera_path):
    command_str = f"python ./dummy.py {model_path} {camera_path} " + time().strftime("%m/%d%Y %H:%M:%S")
    output = subprocess.check_output([command_str], shell=True)
    print(output.decode("utf-8"))


def TaskJob():
    while True:
        cur_cursor.execute(sql_get_config)
        result_set = cur_cursor.fetchall()

        thread_list = []

        for conf in result_set:
            curr_thread = threading.Thread(target=executeModel, args=(conf[2], None))
            thread_list.append(curr_thread)

            curr_thread.start()

        for th in thread_list:
            th.join()

        print("One cycle done.")


TaskJob()
