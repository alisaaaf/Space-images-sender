import telebot
from telebot import types
from functions import get_images
from environs import Env
import schedule
env = Env()
env.read_env()
import time


bot = telebot.TeleBot(env.str("TOKEN"))

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, text=message.text)

@bot.message_handler(commands=['publish_text'])
def publish_text(message):
    bot.send_message('@spaceee_photo', 'Привет! Это тестовое сообщение.')

@bot.message_handler(commands=['publish_photo'])
def publish_photo(message):
    images = get_images()
    media = []
    for image in images:
        media.append(types.InputMediaPhoto(image))
        try:

            bot.send_photo('@spaceee_photo', image)

        except telebot.apihelper.ApiTelegramException:
            pass
    bot.send_media_group(media)
    bot.send_message('367776474', 'Фото опубликованы успешно')

schedule.every().day.at("07:00").do(publish_text)
while True:
    schedule.run_pending()
    time.sleep(1)
