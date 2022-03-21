import telegram.ext

TOKEN ="5201783249:AAGzZhrSXQQc3QlGBfrMQhWO9snyR37dWr8"

def send_message_job(context):
    context.bot.send_message(chat_id='-757413211',text='job executed')

def start(update, context):
    update.message.reply_text("""
    The following commands are avaible:
    """)

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher
disp.add_handler(telegram.ext.CommandHandler("start", start))


job_queue = updater.job_queue
job_queue.run_repeating(send_message_job,interval=10.0,first=0.0)

updater.start_polling()
updater.idle()
