from api.api_bot_site import bot
from aiogram import types
from module import func_weather, lat, lon
import requests
from api.api_bot_site import weather_token


def func_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_hello = types.KeyboardButton("Поздороваться👋")
    btn_name = types.KeyboardButton('Как тебя Зовут?🤔')
    btn_weather = types.KeyboardButton("Узнать погоду в моем городе⛅")
    btn_another_city = types.KeyboardButton("Узнать погоду в другом городе⛅")
    btn_question = types.KeyboardButton("Задать вопрос❓")
    markup.add(btn_hello, btn_name, btn_weather, btn_another_city, btn_question)
    return markup


@bot.message_handler(commands=['start', 'help'])
def start_bot(message):
    bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}.'
                                           f'\nЯ бот Который узнает погоду во всем мире.'
                                           f'\nЧтобы узнать погоду на сегодня нажмите "Узнать погоду в моем городе⛅"',
                     reply_markup=[func_keyboard()])


@bot.message_handler(content_types='text')
def commune(message: types.Message):
    if message.text == 'Поздороваться👋':
        bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}', reply_markup=[func_keyboard()])

    elif message.text == 'Как тебя Зовут?🤔':
        bot.send_message(message.from_user.id, 'Меня зовут Чаппи')

    elif message.text == 'Узнать погоду в моем городе⛅':
        api_weather = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_token}&units=metric'
        )
        data = api_weather.json()
        temp = data['main']['temp']
        bot.send_message(message.from_user.id,  f'Погода в товем городе {temp}',
                         reply_markup=[func_keyboard()])

    elif message.text == 'Узнать погоду в другом городе⛅':
        bot.send_message(message.from_user.id, 'В каком городе хотели узнать погоду⛅:',
                         reply_markup=[func_keyboard()])
        bot.register_next_step_handler(message, weather)

    elif message.text == 'Задать вопрос❓':
        pass


def weather(message):
    text = message.text
    w = func_weather(text)
    bot.send_message(message.from_user.id, f'{w}')


bot.polling(none_stop=True, interval=0)
