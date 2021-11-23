from function import latin_text, translit
import telebot
from translate import to_cyrillic


TOKEN = "2103506248:AAEA1Tjw5rGHiRZyZKI96-DbhNGfskjijg4"
bot = telebot.TeleBot(token=TOKEN)

# number = list(input('Natural son kiriting: '))


@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Bu usul bilan foydalanuvchi nomini olishimiz mumkin
    username = message.from_user.username
    xabar = f"Assalom alaykum, {username}. Sonni textga yozib beruvchi botga xush kelibsiz"
    xabar += '\nSonni yuboring.'
    bot.reply_to(message, xabar)

@bot.message_handler(func=lambda msg: msg.text is not None)
def trans(message):
    msg = message.text
    def javob(msg): return latin_text(msg)
    def kirill(msg): return translit(latin_text(msg))
    all_text = f"O'zbekcha: {javob(msg)}\nKirillcha: {kirill(msg)}\n\n@diyoradm :)"
    bot.reply_to(message, text=all_text)


bot.polling()
# print(latin_text(number))
# print(translit(latin_text(number)))
