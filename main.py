import telebot
import wikipedia
from dotenv import load_dotenv
import os

load_dotenv()
bot = telebot.TeleBot(os.environ.get("TELEGRAM_KEY"))


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Ask me anything, I'll browser wikipedia for you.")


@bot.message_handler()
def reply(message):
    reply = "Could'nt find any information."
    try:
        reply = wikipedia.summary(message.text)
    except Exception:
        pass
    finally:
        bot.reply_to(message, reply)


print("Running...")
bot.infinity_polling()
print("Stopped")
