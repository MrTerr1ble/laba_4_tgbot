import qrcode
import telebot

bot = telebot.TeleBot('6620697996:AAFmLbWf_GI04C-AYu2ONHY4M9H5ODcnMU4')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Hello! Please enter a URL or send a QR code image.')
@bot.message_handler(commands=['help'])
def show_help(message):
    help_text = (
        "Welcome to the QR Code Generator Bot!\n"
        "To generate a QR code, simply enter a valid URL.\n\n"
        "Commands:\n"
        "/start - Start the bot\n"
        "/help - Display this help message"
    )
    bot.send_message(message.chat.id, help_text)

@bot.message_handler(func=lambda message: True)
def handle_user(message):
    if message.text.lower() == 'start':
        send_welcome(message)
    elif message.text.lower() == 'help':
        show_help(message)
    elif message.text.lower().startswith('http'):
        send_qrcode(message)
    else:
        bot.reply_to(message, 'Invalid input. Please enter a valid URL or send a QR code image.')

def send_qrcode(message):

    url = message.text.strip()
    img = qrcode.make(url)
    img.save('qrcode.png')

    with open('qrcode.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)


bot.polling()

