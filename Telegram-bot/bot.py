
import telegram.ext
import sqlite3
from datetime import datetime, timedelta,time


TOKEN = "5201783249:AAGzZhrSXQQc3QlGBfrMQhWO9snyR37dWr8"

connection = sqlite3.connect('../django-app/aOHS/db.sqlite3', check_same_thread=False)
cursor = connection.cursor()

get_violations = "select v.id,  m.name, v.capture " \
                 "from backend_violation v " \
                 "join backend_model m on m.id = v.modelId_id " \
                 "where v.isNotified = 0 " \
                 "limit 3 "


get_specific_worker_vioaltions = "select v.id, w.name, m.name, v.capture " \
                 "from backend_violation v " \
                 "join backend_worker w on w.id = v.workerId_id " \
                 "join backend_model m on m.id = v.modelId_id " \
                 "where w.id = ?"

get_violations_by_date = "select v.id, w.name, m.name, v.capture , v.created " \
                     "from backend_violation v " \
                         "join backend_worker w on w.id = v.workerId_id " \
                             "join backend_model m on m.id = v.modelId_id " \
                                 "where v.created between ? and ? "

set_notified = "update backend_violation " \
               "set isNotified = 1 " \
               "where id = ? "

get_configurations = "select c1.name, m.name " \
                     "from backend_configuration c  " \
                     "join backend_model m on c.modelId_id = m.id " \
                     "join backend_camera c1 on c.cameraId_id = c1.id "

def send_message_job(context):
    cursor.execute(get_violations)
    violations_result_set = cursor.fetchall()

    for violation in violations_result_set:
        context.bot.send_message(chat_id='-757413211', text=f"someone is violating the {violation[1]} rule.")
        cursor.execute(set_notified, (violation[0],))
        connection.commit()
        if violation[2] is not None:
            context.bot.send_photo(chat_id='-757413211',photo=open("../django-app/aOHS/static/images/" + violation[2], 'rb'))


def start(update, context):
    update.message.reply_text("""
        Bot has started!!!
    """)

def help(update, context):
    update.message.reply_text("""
        The following commands are avaible:
                /start : starts the bot
                /worker {id} : shows the violations of the worker with the id
                /cameras : shows the cameras
                /workers : shows the workers
                /models : shows the models
                /violations {date} : shows the violations on the given date with the parameter. Parameters can be today, lastweek, lastmonth, lastyear
                /configurations : shows the configurations
    """)


def worker(update,context):
    workerid = (" ".join(context.args))
    cursor.execute(get_specific_worker_vioaltions, (workerid))
    violations_result_set = cursor.fetchall()
    if len(violations_result_set)>0:
        #update.message.reply_text(f" violation {len(violations_result_set)} violations are  occurred by {violations_result_set[0][1]}")
        #context.bot.send_message(chat_id='-757413211', text=f"{len(violations_result_set)} is violating the {violations_result_set[0][1]} rule.")
        context.bot.send_message(chat_id='-757413211', text=f"{violations_result_set[0][1]} has {len(violations_result_set)} violations.")
        for violation in violations_result_set:
            context.bot.send_message(chat_id='-757413211', text=f"{violation[1]} has violated {violation[2]} rule.",timeout=20) # timeout bir daha bakılabilir
            if violation[3] is not None:
                context.bot.send_photo(chat_id='-757413211', photo=open("../django-app/aOHS/static/images/" + violation[3], 'rb'))
            #update.message.reply_text(f"{violation[1]}  violated the {violation[2]}")

def cameras(update, context):
    cursor.execute("select name,active from backend_camera")
    cameras_result_set = cursor.fetchall()
    context.bot.send_message(chat_id='-757413211', text=f"There are {len(cameras_result_set)} cameras.")
    for camera in cameras_result_set:
        if camera[1] == True:
            context.bot.send_message(chat_id='-757413211', text=f"{camera[0]} is active.")
        else:
            context.bot.send_message(chat_id='-757413211', text=f"{camera[0]} is not active.")

def workers(update, context):
    cursor.execute("select name from backend_worker")
    workers_result_set = cursor.fetchall()
    context.bot.send_message(chat_id='-757413211', text=f"There are {len(workers_result_set)} workers.")
    for worker in workers_result_set:
        context.bot.send_message(chat_id='-757413211', text=f" {worker[0]} ")

def models(update, context):
    cursor.execute("select name from backend_model")
    models_result_set = cursor.fetchall()
    context.bot.send_message(chat_id='-757413211', text=f"There are {len(models_result_set)} models.")
    for model in models_result_set:
        context.bot.send_message(chat_id='-757413211', text=f" {model[0]} ")

def configurations(update, context):
    cursor.execute(get_configurations)
    configurations_result_set = cursor.fetchall()
    context.bot.send_message(chat_id='-757413211', text=f"There are {len(configurations_result_set)} configurations.")
    for configuration in configurations_result_set:
        context.bot.send_message(chat_id='-757413211', text=f" camera: {configuration[0]}, model: {configuration[1]} ")


def violations(update, context):
    param = (" ".join(context.args))
    if param == "today":
        cursor.execute(get_violations_by_date, (datetime.now(), datetime.now() -timedelta(days=1)))
    elif param == "lastweek":
        cursor.execute(get_violations_by_date, (datetime.now()-timedelta(days=7), datetime.now()))
    elif param == "lastmonth":
        cursor.execute(get_violations_by_date, (datetime.now()-timedelta(days=30), datetime.now()))
    elif param == "lastyear":
        cursor.execute(get_violations_by_date, (datetime.now()-timedelta(days=365), datetime.now()))

    violations_result_set = cursor.fetchall()
    context.bot.send_message(chat_id='-757413211', text=f"{param},There are {len(violations_result_set)} violations.")
    for violation in violations_result_set:
        context.bot.send_message(chat_id='-757413211', text=f"{violation[1]} has violated {violation[2]} rule at {violation[4][:19]}.",timeout=20)
        if violation[3] is not None:
            context.bot.send_photo(chat_id='-757413211', photo=open("../django-app/aOHS/static/images/" + violation[3], 'rb'))

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher
disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("worker", worker))
disp.add_handler(telegram.ext.CommandHandler("cameras", cameras))
disp.add_handler(telegram.ext.CommandHandler("workers", workers))
disp.add_handler(telegram.ext.CommandHandler("models", models))
disp.add_handler(telegram.ext.CommandHandler("violations", violations))
disp.add_handler(telegram.ext.CommandHandler("configurations", configurations))
job_queue = updater.job_queue
job_queue.run_repeating(send_message_job, interval=10.0, first=0.0)



updater.start_polling()
updater.idle()
