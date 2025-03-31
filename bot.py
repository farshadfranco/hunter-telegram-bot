
import os
import telebot

TOKEN = os.getenv("TELEGRAM_TOKEN")
GROUP_ID = int(os.getenv("GROUP_ID"))

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: message.chat.id == GROUP_ID)
def handle_message(message):
    if message.from_user.is_bot:
        return

    text = message.text.lower()
    if "سلام" in text:
        bot.reply_to(message, "سلام! من هانترم، پایه‌ی گپ و خنده‌ام!")
    elif "هانتر" in text:
        bot.reply_to(message, "جون دلم؟ باهاتم!")
    else:
        bot.reply_to(message, "ایول! بزن بریم یه گپی بزنیم.")

bot.polling()
