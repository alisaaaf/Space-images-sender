import telebot
from functions import get_images
import os
from environs import Env
import schedule
env = Env()
env.read_env()
import time


bot = telebot.TeleBot(env.str("TOKEN"))

@bot.message_handler(commands=['start1'])
def start_message(message):
    bot.reply_to(message, text=message.text)

@bot.message_handler(commands=['publish_text'])
def publish_text(message):
    bot.send_message('@spaceee_photo', 'Привет! Это тестовое сообщение.')

@bot.message_handler(commands=['publish_photo'])
def publish_photo(message):
    images = get_images()
    for image in images:
        try:
            bot.send_photo('@spaceee_photo', image)

        except telebot.apihelper.ApiTelegramException:
            pass

    bot.send_message('367776474', 'Фото опубликованы успешно')

bot.polling()

schedule.every().day.at("19:42").do(publish_photo)
