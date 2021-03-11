# load environment
import os
from dotenv import load_dotenv
load_dotenv()
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

updater = Updater(token=os.getenv('TELEGRAM_TOKEN'), use_context=True)

dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#displays this to the user when the start command is executed
def start(update, context):
    user = update.effective_user.id # id of the user who sent the message
    context.bot.send_message(chat_id=update.effective_chat.id, text="""
    Welcome to COVID-19 Vaccination Tracker""")
 
   
def message(update, context):
    user = update.effective_user.id # id of the user who sent the message
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
 
 #This handles the start command   
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

message_handler = MessageHandler(Filters.text & (~Filters.command), message)
dispatcher.add_handler(message_handler)

updater.start_polling()