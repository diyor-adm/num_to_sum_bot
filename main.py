import telebot 
import logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG)
TOKEN = "5355512939:AAGoOP16TsX022x-x_wPjYBaB5zF1rWYNNg"
bot = telebot.TeleBot(token=TOKEN)

# \start komandasi uchun mas'ul funksiya
@bot.message_handler(commands=['start'])
def send_welcome(message):
    username = message.from_user.username # Bu usul bilan foydalanuvchi nomini olishimiz mumkin
    xabar = f"Ассалому алайкум, {username}. \nMoka.uz интернет бозорининг сотув ботига хуш келибсиз."
    bot.reply_to(message, xabar)
    xabar2 = '\nСиз кидираётган нарса бизда бор ва уни сиз "Каталог" оркали топишингиз мумкин😉'
    bot.send_message(message.chat.id, xabar2)

# matnlar uchun mas'ul funksiya
@bot.message_handler()
def translit(message):
    javob = 'Илтимос "Каталог" оркали кидиринг)'
    bot.reply_to(message, javob)
    

bot.polling()
