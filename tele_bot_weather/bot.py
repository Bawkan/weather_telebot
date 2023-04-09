from api.api_bot_site import dp, weather_token
from aiogram import types, executor
from module import func_weat



def func_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_hello = types.KeyboardButton("Поздороваться👋")
    btn_name = types.KeyboardButton('Как тебя Зовут?🤔')
    btn_weather = types.KeyboardButton("Узнать погоду в моем городе⛅")
    btn_another_city = types.KeyboardButton("Узнать погоду в другом городе⛅")
    btn_question = types.KeyboardButton("Задать вопрос❓")
    markup.add(btn_hello, btn_name, btn_weather, btn_another_city, btn_question)
    return markup


@dp.message_handler(commands=['start', 'help'])
async def start_bot(message):
    await message.reply(f'Привет {message.from_user.first_name}.\nЯ бот Который узнает погоду во всем мире.'
                        f'\nЧтобы узнать погоду на сегодня нажми "Узнать погоду в моем городе⛅"',
                        reply_markup=func_keyboard())


response = func_weat()


@dp.message_handler(content_types='text')
async def commune(message: types.Message):
    if message.text == 'Поздороваться👋':
        await message.reply(f'Привет {message.from_user.first_name}')

    elif message.text == 'Как тебя Зовут?🤔':
        await message.reply('Меня зовут Чаппи')

    elif message.text == 'Узнать погоду в моем городе⛅':
        await message.reply('weather in your city: ', response)

    elif message.text == 'Узнать погоду в другом городе⛅':
        pass

    elif message.text == 'Задать вопрос❓':
        pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
