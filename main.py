import os
import telebot

bot = telebot.TeleBot("5198668161:AAFa6_zqbCu7P70h_2H9ogBZN7AC8l2T3yU")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Hello! I am 𝐀𝐧𝐝𝐫𝐨𝐢𝐝 𝐀𝐩𝐩 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐁𝐨𝐭")

@bot.message_handler(commands=["whatsapp_business"])
def send_welcome(message):
    bot.reply_to(message,"https://play.google.com/store/apps/details?id=com.whatsapp.w4b")

@bot.message_handler(commands=["telegram"])
def send_welcome(message):
    bot.reply_to(message,"https://play.google.com/store/apps/details?id=org.telegram.messenger")

@bot.message_handler(commands=["facebook_lite"])
def send_welcome(message):
    bot.reply_to(message,"https://play.google.com/store/apps/details?id=com.facebook.lite")

@bot.message_handler(commands=["imo"])
def send_welcome(message):
    bot.reply_to(message,"https://play.google.com/store/apps/details?id=com.imo.android.imoim")

@bot.message_handler(commands=["skype"])
def send_welcome(message):
    bot.reply_to(message,"https://play.google.com/store/apps/details?id=com.skype.raider")

@bot.message_handler(commands=["zoom"])
def send_welcome(message):
    bot.reply_to(message,"https://play.google.com/store/apps/details?id=us.zoom.videomeetings")

bot.polling()
