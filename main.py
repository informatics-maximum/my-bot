from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
import logging

updater = Updater(token='5516783193:AAHj5EtYY6iaq4ydfkFAUx-ti3jOHHujlnM')
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def echo(update: Update, context: CallbackContext):
    text = update.message.text
    text_with_empty_strings = ''
    for i in range(len(text)):
        text_with_empty_strings += text[i]
        if text[i]=="\n":
            text_with_empty_strings += "\n"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_with_empty_strings)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
#updater.stop()