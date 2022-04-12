import telegram.ext
import sqlite3

TOKEN = "5201783249:AAGzZhrSXQQc3QlGBfrMQhWO9snyR37dWr8"

connection = sqlite3.connect('../django-app/aOHS/db.sqlite3', check_same_thread=False)
cursor = connection.cursor()

get_violations = "select v.id, w.name, m.name " \
                 "from backend_violation v " \
                 "join backend_worker w on w.id = v.workerId_id " \
                 "join backend_model m on m.id = v.modelId_id " \
                 "where v.isNotified = 0 " \
                 "limit 3 "


get_workers_violations = "select v.id, w.name, m.name " \
                 "from backend_violation v " \
                 "join backend_worker w on w.id = v.workerId_id " \
                 "join backend_model m on m.id = v.modelId_id " \
                 "limit 3 "


get_specific_worker_vioaltions = "select v.id, w.name, m.name " \
                 "from backend_violation v " \
                 "join backend_worker w on w.id = v.workerId_id " \
                 "join backend_model m on m.id = v.modelId_id " \
                 "where w.id = ?"

set_notified = "update backend_violation " \
               "set isNotified = 1 " \
               "where id = ? "


def send_message_job(context):
    cursor.execute(get_violations)
    violations_result_set = cursor.fetchall()

    for violation in violations_result_set:
        context.bot.send_message(chat_id='-757413211', text=f"{violation[1]} is violating the {violation[2]} rule.")
        cursor.execute(set_notified, (violation[0],))

def get_workers_violations(update, context):
    cursor.execute(get_workers_violations)
    violations_result_set = cursor.fetchall()

    for violation in violations_result_set:
        update.message.reply_text(f"{violation[1]} violated the {violation[0]}.")


def start(update, context):
    update.message.reply_text("""
    The following commands are avaible:
    """)


def worker(update,context):
    workerid = (" ".join(context.args))
    cursor.execute(get_specific_worker_vioaltions, (workerid))
    violations_result_set = cursor.fetchall()
    if len(violations_result_set)>0:
        update.message.reply_text(f" violation {len(violations_result_set)} violations are  occurred by {violations_result_set[0][1]}")
        for violation in violations_result_set:
            update.message.reply_text(f"{violation[1]}  violated the {violation[2]}")






updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher
disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("violations", get_workers_violations))
disp.add_handler(telegram.ext.CommandHandler("worker", worker))
#job_queue = updater.job_queue
#job_queue.run_repeating(send_message_job, interval=10.0, first=0.0)



updater.start_polling()
updater.idle()
