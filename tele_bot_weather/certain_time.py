from api.api_bot_site import bot
import time
import requests
from api.api_bot_site import weather_token
from module import lat, lon


def weather_every_day():
    api_weather = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_token}&units=metric"
    )
    data = api_weather.json()
    temp = data["main"]["temp"]
    return f"Погода в товем городе {temp}"


def time_weather(message):
    weather = weather_every_day()
    while True:
        bot.send_message(message.chat.id, f'{weather}')
        time.sleep(3)


if __name__ == "__main__":
    time_weather()
