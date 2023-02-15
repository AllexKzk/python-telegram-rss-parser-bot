import telebot
import time
from threading import Thread
import sites
import checking #server part for replit!

bot = telebot.TeleBot("")
ss42Id = #Id
ss42IdTest = #IdFotTest


@bot.message_handler(commands=['start'])
def send_message(message):  
  print(message.chat_id)

def update_news():
    while True:
        for site in sites.parseDict.keys():
            post = sites.parse(site)
            if post:
                title = post["title"]
                source = post["link"]
                bot.send_message(
                  ss42Id,
                  f"<b>{title}:</b>\n<a href = \"{source}\">[Source]</a>",
                  parse_mode="HTML")
        time.sleep(800) #check sites for updates per 800s


checking.checking()

update_news()

Thread(target=bot.infinity_polling).start()