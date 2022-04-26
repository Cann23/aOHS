
import telegram.ext
import sqlite3



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

set_notified = "update backend_violation " \
               "set isNotified = 1 " \
               "where id = ? "


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
                /start
                /worker {id}
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






updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher
disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("worker", worker))
job_queue = updater.job_queue
job_queue.run_repeating(send_message_job, interval=10.0, first=0.0)



updater.start_polling()
updater.idle()
