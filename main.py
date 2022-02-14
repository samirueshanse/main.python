import os
import telebot

bot = telebot.TeleBot("5198668161:AAFa6_zqbCu7P70h_2H9ogBZN7AC8l2T3yU")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Hello! I am 𝐀𝐧𝐝𝐫𝐨𝐢𝐝 𝐀𝐩𝐩 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐁𝐨𝐭"
                         "Use my menu")

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

@bot.message_handler(commands=["tiktok"])
def send_welcome(message):
    bot.reply_to(message,"https://play.google.com/store/apps/details?id=com.zhiliaoapp.musically")

@bot.message_handler(commands=["messanger_lite"])
def send_welcome(message):
    bot.reply_to(message,"https://play.google.com/store/apps/details?id=com.facebook.mlite")

@bot.message_handler(commands=["youtube"])
def send_welcome(message):
    bot.reply_to(message,"https://play.google.com/store/apps/details?id=com.google.android.youtube")

@bot.message_handler(commands=["twitter"])
def send_welcome(message):
    bot.reply_to(message,"https://play.google.com/store/apps/details?id=com.twitter.android")

@bot.message_handler(commands=["microsoft_edge"])
def send_welcome(message):
    bot.reply_to(message,"https://play.google.com/store/apps/details?id=com.microsoft.emmx")

@bot.message_handler(commands=["google_play_games"])
def send_welcome(message):
    bot.reply_to(message,"https://play.google.com/store/apps/details?id=com.google.android.play.games")

@bot.message_handler(commands=["help"])
def send_welcome(message):
    bot.reply_to(message,"Use my menu")

bot.polling()
