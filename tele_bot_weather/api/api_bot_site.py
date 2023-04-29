import telebot
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
bot = telebot.TeleBot(os.getenv('BOT'))

weather_token = os.getenv('WEATHER_API')
