



from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

updater = Updater(token=config["telegram_token"], use_context=True)

dispatcher = updater.dispatcher

#displays this to the user when the start command is executed
def start(update, context):
  user = update.effective_user.id # id of the user who sent the message
  context.bot.send_message(chat_id=update.effective_chat.id, text="""
  Welcome to Word Puzzle Game""")
 
   
def message(update, context):
  print(context.bot_data)
  print(context.chat_data)
  print(context.user_data)
  print(context.bot)
  user = update.effective_user.id # id of the user who sent the message
  context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
 
 #This handles the start command   
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

message_handler = MessageHandler(Filters.text & (~Filters.command), message)
dispatcher.add_handler(message_handler)

updater.start_polling()


class Bot:
  def __init__(self):
    pass