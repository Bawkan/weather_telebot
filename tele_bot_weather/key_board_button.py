from aiogram import types


def func_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_hello = types.KeyboardButton("Поздороваться👋")
    btn_weather = types.KeyboardButton("Узнать погоду в моем городе⛅")
    btn_another_city = types.KeyboardButton("Узнать погоду в другом городе⛅")
    certain_time = types.KeyboardButton("Отправка погоды каждый час⛅")
    btn_question = types.KeyboardButton("Задать вопрос❓")
    markup.add(btn_hello, btn_weather, btn_another_city, certain_time, btn_question)
    return markup


def questions():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_name = types.KeyboardButton("Как тебя Зовут?🤔")
    btn_back = types.KeyboardButton("Назад🔙")
    markup.add(btn_name, btn_back)
    return markup
