from api.api_bot_site import bot
from aiogram import types
from module import lat, lon, weather
from certain_time import time_weather
import requests
from api.api_bot_site import weather_token
import sqlite3
from key_board_button import func_keyboard, questions


@bot.message_handler(commands=["start", "help"])
def start_bot(message):
    bot.send_message(
        message.from_user.id,
        f"Привет {message.from_user.first_name}."
        f"\nЯ бот Который узнает погоду во всем мире."
        f'\nЧтобы узнать погоду на сегодня нажмите "Узнать погоду в моем городе⛅"',
        reply_markup=[func_keyboard()],
    )


@bot.message_handler(content_types="text")
def commune(message: types.Message):
    connect = sqlite3.connect("orders.db")
    cursor = connect.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS login_id(
        id INTEGER
        )"""
    )
    connect.commit()

    user_id = [message.chat.id]
    cursor.execute("INSERT INTO login_id VALUES(?);", user_id)
    connect.commit()

    if message.text == "Поздороваться👋":
        bot.send_message(
            message.from_user.id,
            f"Привет {message.from_user.first_name}",
            reply_markup=[func_keyboard()],
        )

    elif message.text == "Как тебя Зовут?🤔":
        bot.send_message(message.from_user.id, "Меня зовут Чаппи")

    elif message.text == "Узнать погоду в моем городе⛅":
        api_weather = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_token}&units=metric"
        )
        data = api_weather.json()
        temp = data["main"]["temp"]
        bot.send_message(
            message.from_user.id,
            f"Погода в товем городе {temp}",
            reply_markup=[func_keyboard()],
        )

    elif message.text == "Узнать погоду в другом городе⛅":
        bot.send_message(
            message.from_user.id,
            "В каком городе хотели узнать погоду⛅:",
            reply_markup=[func_keyboard()],
        )
        bot.register_next_step_handler(message, weather)

    elif message.text == "Задать вопрос❓":
        bot.send_message(
            message.from_user.id,
            f"Слушаю вас{message.from_user.first_name}🤖",
            reply_markup=[questions()],
        )
    elif message.text == "Как тебя Зовут?🤔":
        bot.send_message(message.from_user.id, "Меня зовут Чаппи")

    elif message.text == "Назад🔙":
        bot.send_message(
            message.from_user.id,
            "Вы вернулись в начало",
            reply_markup=[func_keyboard()],
        )

    elif message.text == "Отправка погоды каждый час⛅":
        bot.send_message(
            message.from_user.id,
            "Вам будет отправлена погода каждый час,хорошего дня 😉",
            reply_markup=[func_keyboard()],
        )

        time_weather(message)

    else:
        bot.send_message(
            message.chat.id, text="На такую комманду я не запрограммировал бота"
        )


bot.polling(none_stop=True, interval=0)
