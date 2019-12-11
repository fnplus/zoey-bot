import os
import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import InlineQueryHandler
from telegram.ext import MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent

updater = Updater(token=os.environ.get('TOKEN', None), use_context=True)
dp = updater.dispatcher

def print_commands(commands):
    str = commands[0] + ", "
    for i in range(1, len(commands) - 1):
        str += commands[i] + ", "

    str += "and " + commands[-1]

    return str


commands = ['start', 'cat', 'meow', 'help']

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

def start(bot, context):
    context.bot.send_message(chat_id=bot.effective_chat.id, text="Hi! I'm Zoey and I'm part of fn+geeks community. I don't talk much right now. Meow")

def cat(bot, context):
    context.bot.send_message(chat_id=bot.effective_chat.id, text="🐈🐾")

def meow(bot, context):
    context.bot.send_message(chat_id=bot.effective_chat.id, text="🐈🐾")

def help(bot, context):
    context.bot.send_message(chat_id=bot.effective_chat.id, text="Don't be afraid. I'm just a cat. Purrr")

def unknown(bot, context):
    context.bot.send_message(chat_id=bot.effective_chat.id, text=f"Sorry, I didn't understand that command. My available commands are {print_commands(commands)}")


dp.add_handler(CommandHandler('cat', cat))
dp.add_handler(CommandHandler('meow', meow))
dp.add_handler(CommandHandler('help', help))
dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.command, unknown))


# Polling
updater.start_polling()
updater.idle()
