import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import InlineQueryHandler
from telegram.ext import MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent

updater = Updater(token="975930481:AAFUEWivRle21qs2rdj84RynSf4-78WXJVg", use_context=True)
dp = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I'm Zoey and I'm part of fn+geeks community. I don't talk much right now. Meow")

def cat(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="🐈🐾")

def meow(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="🐈🐾")

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Don't be afraid. I'm just a cat. Purrr")

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

dp.add_handler(CommandHandler('cat', cat))
dp.add_handler(CommandHandler('meow', meow))
dp.add_handler(CommandHandler('help', help))
dp.add_handler(CommandHandler('start', start))

# Filters.command must be added last
# dp.add_handler(MessageHandler(Filters.command, unknown))

# Polling
updater.start_polling()