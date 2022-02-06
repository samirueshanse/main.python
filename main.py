import os
import telebot

bot = telebot.TeleBot("5223814916:AAFFbc5LR94uaRh8lXCDrudY-uX1IyXbbHQ")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Hello! I am Management Chat BOT")

@bot.message_handler(commands=["group"])
def send_welcome(message):
    bot.reply_to(message,"https://t.me/Anytime_Sri_Lankan_link_Share")

@bot.message_handler(commands=["newbot"])
def send_welcome(message):
    bot.reply_to(message,"Go to the Botfather. And create the bot https://t.me/BotFather")

@bot.message_handler(commands=["owner"])
def send_welcome(message):
    bot.reply_to(message,"https://t.me/Spider_Man_Super")

#send_photo
@bot.on_message(filters.command("photo"))
def command3(bot, message):
    bot.send_photo(message.chat.id, "content://com.android.chrome.FileProvider/images/screenshot/1644128040450828178238706960328.jpg")

bot.polling()
