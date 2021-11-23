from function import latin_text, translit
from translate import to_cyrillic
# telegram
from telegram.ext import Updater, CommandHandler, dispatcher,CallbackContext, MessageHandler
from telegram.ext.filters import Filters
from telegram.update import Update
from googletrans import Translator


updater = Updater(token='2103506248:AAEA1Tjw5rGHiRZyZKI96-DbhNGfskjijg4')



def send_welcome(update: Update, context: CallbackContext):
   update.message.reply_text('Assalomu alaykum, sonni matn ko`rinishiga o`tkazuvchi botga xush kelibsiz!')
   update.message.reply_text("Iltimos kerakli matn tilini tanlagandan so`ng sonni kiriting.\nMisol uchun:\nO`zbekcha matn uchun - /uz 123\nKirillcha matn uchun - /kr 123\nRuscha matn uchun - /ru 123\nInglizcha matn uchun - /en 123\n\nBot yaratuvchisi haqida batafsil /about buyrug`i orqali bilib olishingiz mumkin!")
def all_message(update: Update, context: CallbackContext):
   update.message.reply_text("Iltimos kerakli matn tilini tanlagandan so`ng sonni kiriting.\nMisol uchun:\nO`zbekcha matn uchun - /uz 123\nKirillcha matn uchun - /kr 123\nRuscha matn uchun - /ru 123\nInglizcha matn uchun - /en 123")

# def trans(message):
#     msg = message.text
#     def javob(msg): return latin_text(msg)
#     def kirill(msg): return translit(latin_text(msg))
#     all_text = f"O'zbekcha: {javob(msg)}\nKirillcha: {kirill(msg)}\n\n@diyoradm :)"
#     bot.reply_to(message, text=all_text)
def uz_text(update: Update, context: CallbackContext):
    args = context.args
    if len(args)==0:
        update.message.reply_text('Hech bo`lmasa bitta son yozing!')
    else:
        javob = text_sum(args)
        update.message.reply_text(javob)

def text_sum(args):
    print(args)
    message = []
    for i in args:
        message +=i
    def javob(message): return latin_text(message)
    return javob(message)
    
        

def kr_text(update: Update, context: CallbackContext):
    args = context.args
    if len(args)==0:
        update.message.reply_text('Hech bo`lmasa bitta son yozing!')
    else:
        update.message.reply_text(to_cyrillic(text_sum(args)))

def en_text(update: Update, context: CallbackContext):
    args = context.args
    if len(args)==0:
        update.message.reply_text('Hech bo`lmasa bitta son yozing!')
    else:
        matn = text_sum(args)
        translator = Translator()
        matn = translator.translate(matn, dest='en').text
        print(matn)
        update.message.reply_text(matn)

def ru_text(update: Update, context: CallbackContext):
    args = context.args
    if len(args)==0:
        update.message.reply_text('Hech bo`lmasa bitta son yozing!')
    else:
        matn = text_sum(args)
        translator = Translator()
        matn = translator.translate(matn, dest='ru').text
        print(matn)
        update.message.reply_text(matn)

def about(update: Update, context: CallbackContext):
    update.message.reply_text('Ushbu bot Diyorbek Abduqodirov tomonidan ishlab chiqildi. \n@diyoradm')



dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', send_welcome))
dispatcher.add_handler(CommandHandler('uz', uz_text))
dispatcher.add_handler(CommandHandler('kr', kr_text))
dispatcher.add_handler(CommandHandler('en', en_text))
dispatcher.add_handler(CommandHandler('ru', ru_text))
dispatcher.add_handler(CommandHandler('about', about))
dispatcher.add_handler(MessageHandler(Filters.all, all_message))





updater.start_polling()
updater.idle()


# def kirill(message): return translit(latin_text(message))
# all_text = f"O'zbekcha: {javob(message)}\nKirillcha: {kirill(message)}\n\n@diyoradm :)"