from api.api_bot_site import weather_token
import requests
from urllib.request import urlopen
import json
from api.api_bot_site import bot


def _get_ip_data() -> dict:
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    return json.load(response)


data = _get_ip_data()
lat = data['loc'].split(',')[0]
lon = data['loc'].split(',')[1]


def func_weather(city):
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}&units=metric'
    )
    data = r.json()
    try:
        name = data['name']
        temp = data['main']['temp']
        return f'Погода в {name} {temp} C'
    except:
        return 'такого города нет'


if __name__ == '__main__':
    func_weather()
