from telegram import user
from function import latin_text, translit
from settings.local_settings import TELEGRAM_TOKEN
from translate import to_cyrillic
# telegram
from telegram.ext import Updater, Dispatcher, CommandHandler, callbackcontext, dispatcher
from telegram.update import Update
from settings import settings


updater = Updater(token=settings.TELEGRAM_TOKEN)


def send_welcome(update: Update, context: callbackcontext):
   update.message.reply_text('Salom!')

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', send_welcome))


# @bot.message_handler(func=lambda msg: msg.text is not None)
# def trans(message):
#     msg = message.text
#     def javob(msg): return latin_text(msg)
#     def kirill(msg): return translit(latin_text(msg))
#     all_text = f"O'zbekcha: {javob(msg)}\nKirillcha: {kirill(msg)}\n\n@diyoradm :)"
#     bot.reply_to(message, text=all_text)


updater.start_polling()
updater.idle()