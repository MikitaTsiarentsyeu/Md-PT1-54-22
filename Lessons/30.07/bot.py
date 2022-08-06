#5548880687:AAGWY-nKfos5Umx6XN7y8DwPejowHFbhJKU

import telebot
from urllib.request import urlopen
from bs4 import BeautifulSoup

bot = telebot.TeleBot("5548880687:AAGWY-nKfos5Umx6XN7y8DwPejowHFbhJKU")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hello there my dear friend, how are you?")

@bot.message_handler(commands=['update'])
def update_message(message):

    html = urlopen("https://kurs.onliner.by/")
    soup = BeautifulSoup(html)

    tags = soup.findAll("p", {"class":"value"})

    buy = tags[0].text
    sell = tags[1].text
    nb = tags[2].text

    bot.send_message(message.chat.id, buy + ", " + sell + ", " + nb)

bot.polling()
