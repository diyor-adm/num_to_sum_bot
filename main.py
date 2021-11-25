from telegram.inline.inputtextmessagecontent import InputTextMessageContent
from function import latin_text
from telegram.ext import Updater,InlineQueryHandler, CommandHandler, dispatcher,CallbackContext, MessageHandler, CallbackQueryHandler
from function import to_cyrillic
from telegram.ext.filters import Filters
from telegram.update import Update
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, ReplyMarkup, replymarkup
import logging
from translate import Translator

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG)

flag = ''
text_flag = '' 
updater = Updater(token='2107634479:AAFqg7_jASoQxjhafYAWJZ464iQNblevQ1I')

def send_welcome(update: Update, context: CallbackContext):
   update.message.reply_text(f'Salom {update.effective_user.first_name}, tilni tanlang!', reply_markup=main_menu_keyboard())
 
def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton("🇺🇿 O'zbekcha", callback_data='uz_latin'),
            InlineKeyboardButton('🇷🇺 Русский', callback_data='rus')],
            [InlineKeyboardButton('🇺🇿 Ўзбекча', callback_data='uzbek_kirill_key'), 
            InlineKeyboardButton('🇬🇧 English ', callback_data='english_key')]]
  return InlineKeyboardMarkup(keyboard)

def uzbek_latin(update: Update, context: CallbackContext):
    global flag
    flag = 'uz'
    update.callback_query.message.edit_text("🇺🇿 O'zbek tili tanlandi!")
    
def uzbek_kirill_key(update: Update, context: CallbackContext):
    global flag
    flag = 'uz_kr'
    update.callback_query.message.edit_text("🇺🇿 Ўзбек тили танланди!")
def rus(update: Update, context: CallbackContext):
    global flag
    flag = 'ru'
    update.callback_query.message.edit_text("🇷🇺 Русский был выбран!")
def english_key(update: Update, context: CallbackContext):
    global flag
    flag = 'en'
    update.callback_query.message.edit_text("🇬🇧 Language has been changed to English")
      
def control(update: Update, context: CallbackContext):
    args = update.effective_message.text
    if flag == 'uz':
        if args.isnumeric():
            args = uz_text(args).capitalize()
            update.message.reply_text(args)
        else:
            update.message.reply_text('Iltimos faqat son kiriting!')
            return 
    elif flag == 'uz_kr':
        if args.isnumeric():
            args = uz_text(args).capitalize()
            update.message.reply_text(to_cyrillic(args))
        else:
            update.message.reply_text('Илтимос факат сон киритинг!')
            return
    elif flag == 'ru':
        if args.isnumeric():
            args = uz_text(args).capitalize()
            translator= Translator(from_lang="uz",to_lang="ru")
            translation = translator.translate(args)
            update.message.reply_text(translation)
        else:
            update.message.reply_text('Пожалуйста, просто введите число')
            return
    elif flag == 'en':
        if args.isnumeric():
            args = uz_text(args).capitalize()
            translator= Translator(from_lang="uz",to_lang="en")
            translation = translator.translate(args)
            update.message.reply_text(translation)
        else:
            update.message.reply_text('Please just enter a number')
            return 
    else:
        update.message.reply_text(f'Iltimos {update.effective_user.first_name}, tilni tanlang!', reply_markup=main_menu_keyboard())


        # if len(args)==0:
        #     update.message.reply_text('Hech bo`lmasa bitta son yozing!')
        # else:
        #     javob = text_sum(args)
        #     update.message.reply_text(javob)

def text_sum(args):
    print(args)
    message = []
    for i in args:
        message +=i
    def javob(message): return latin_text(message)
    return javob(message)






def about(update: Update, context: CallbackContext):
    update.message.reply_text('Ushbu bot Diyorbek Abduqodirov tomonidan ishlab chiqildi. \n@diyoradm')

def uz_text(text):
    javob = text_sum(text)
    return javob

def text_sum(args):
    print(args)
    message = []
    for i in args:
        message +=i
    def javob(message): return latin_text(message)
    return javob(message)
       

def error(update: Update, context: CallbackContext):
    update.message.reply_text('Bot hozirda inline rejimda ishlamoqda, tez orada to`liq ishga tushiramiz. Bizdan uzoqlashmang\n\nTakliflar uchun @diyor_adm ga murojaat qilishingiz mumkin😅')

def inline_query(update: Update, context: CallbackContext):
    query = update.inline_query.query
    with open('all_search.txt','a') as numstxt:
        print(query)
        if query != '':
            numstxt.write(query + f' - @{update.effective_user.username}\n')
    if query.isnumeric():
        text = uz_text(query).capitalize()
        print(text)
        with open('uz_search.txt','a') as numstxt:
            numstxt.write(text + f' - @{update.effective_user.username}\n')
        global text_flag
        text_flag=text
        update.inline_query.answer([
            InlineQueryResultArticle(
                id=text, description=f'Salom {update.effective_user.first_name}  \nMade with 🖤 by @diyoradm',
                title=f'✅ {text}', 
                input_message_content=InputTextMessageContent(text + '\nQuyidagi tugmalarni bosish orqali kerakli tilni tanlang\n@sonnimatngabot'),
                reply_markup=inline_menu_keyboard() )
            ])
    elif (len(query) == 0):
            text = 'Hech bo`lmasa bitta son yozing😁'
            print(text)
            update.inline_query.answer([
                InlineQueryResultArticle(
                    id='a', description=f'Salom {update.effective_user.first_name}  \nMade with 🖤 by @diyoradm',
                    title=f'⛔️ {text}',
                    input_message_content=InputTextMessageContent(text + '\n\n@sonnimatngabot'))
            ])
    else:
        text = '⛔️ Iltimos faqat son yozing'
        update.inline_query.answer([
                InlineQueryResultArticle(
                    id=text, description=f'Salom {update.effective_user.first_name}  \nMade with 🖤 by @diyoradm',
                    title=text,
                    input_message_content=InputTextMessageContent(text))
        ])

def xato_keyboard ():
    keyboard = [[InlineKeyboardButton('Ha', callback_data='trans_error'),
    InlineKeyboardButton('Yo`q', callback_data='trans_correct')]]        
    return InlineKeyboardMarkup(keyboard)

def inline_menu_keyboard():
  keyboard = [[InlineKeyboardButton('🇺🇿 Ўзбекча', callback_data='uz_kirill'), InlineKeyboardButton('🇷🇺 Русский', callback_data='russian'), InlineKeyboardButton('🇬🇧 English ', callback_data='english')]]        
  return InlineKeyboardMarkup(keyboard)
adm =''
def uzbek_kirill(update: Update, context: CallbackContext):
    text = to_cyrillic(text_flag)
    global adm
    adm = text
    print(text)
    with open('kirill_search.txt','a') as numstxt:
            numstxt.write(text + f' - @{update.effective_user.username}\n')
    update.callback_query.edit_message_text(f'{text}\n\nTarjimada xatolik bormi?', reply_markup=xato_keyboard())

def english(update: Update, context: CallbackContext):
    translator = Translator()
    text = translator.translate(text_flag, dest='en').text
    global adm
    adm = text
    print(text)
    with open('eng_search.txt','a') as numstxt:
            numstxt.write(text + f' - @{update.effective_user.username}\n')
    update.callback_query.edit_message_text(f'{text}\n\nTarjimada xatolik bormi?', reply_markup=xato_keyboard())

def russian(update: Update, context: CallbackContext):
    translator = Translator()
    text = translator.translate(text_flag, dest='ru').text
    global adm
    adm = text
    print(text)
    with open('ru_search.txt','a') as numstxt:
            numstxt.write(text + f' - @{update.effective_user.username}\n')
    update.callback_query.edit_message_text(f'{text}\n\nTarjimada xatolik bormi?', reply_markup=xato_keyboard())
def trans_correct(update: Update, context: CallbackContext):
    update.callback_query.edit_message_text(f'Rahmat {update.effective_user.first_name}🤗')
    with open('correct.txt','a') as numstxt:
            numstxt.write( adm + f' - @{update.effective_user.username}\n')
def trans_error(update: Update, context: CallbackContext):
    update.callback_query.edit_message_text(f'Rahmat {update.effective_user.first_name}! Tez orada to`g`irlashga harakat qilamiz😊')
    with open('uncorrect.txt','a') as numstxt:
            numstxt.write( adm + f' - @{update.effective_user.username}\n')
def select_lang(update: Update, context: CallbackContext):
    if flag == 'ru':
        update.message.reply_text(f'{update.effective_user.first_name} выбери нужный язык!', reply_markup=main_menu_keyboard())
    elif flag == 'uz_kr':
        update.message.reply_text(f'{update.effective_user.first_name} керакли тилни танланг!', reply_markup=main_menu_keyboard())
    elif flag == 'en':
        update.message.reply_text(f'{update.effective_user.first_name} choose the language you need!', reply_markup=main_menu_keyboard())
    else:
        update.message.reply_text(f'{update.effective_user.first_name} kerakli tilni tanlang!', reply_markup=main_menu_keyboard())
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', send_welcome))
dispatcher.add_handler(CommandHandler('about', about))
dispatcher.add_handler(CommandHandler('language', select_lang))
dispatcher.add_handler(CallbackQueryHandler(uzbek_latin, pattern='uz_latin'))
dispatcher.add_handler(CallbackQueryHandler(uzbek_kirill, pattern='uz_kirill'))
dispatcher.add_handler(CallbackQueryHandler(uzbek_kirill_key, pattern='uzbek_kirill_key'))
dispatcher.add_handler(CallbackQueryHandler(russian, pattern='russian'))
dispatcher.add_handler(CallbackQueryHandler(rus, pattern='rus'))
dispatcher.add_handler(CallbackQueryHandler(trans_correct, pattern='trans_correct'))
dispatcher.add_handler(CallbackQueryHandler(trans_error, pattern='trans_error'))
dispatcher.add_handler(CallbackQueryHandler(english_key, pattern='english_key'))

dispatcher.add_handler(InlineQueryHandler(inline_query))

dispatcher.add_handler(MessageHandler(Filters.all, control))





updater.start_polling()
updater.idle()


# def kirill(message): return translit(latin_text(message))
# all_text = f"O'zbekcha: {javob(message)}\nKirillcha: {kirill(message)}\n\n@diyoradm :)"