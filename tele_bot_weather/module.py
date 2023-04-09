from api.api_bot_site import weather_token
import requests
from urllib.request import urlopen
import json

def _get_ip_data() -> dict:
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    return json.load(response)


data = _get_ip_data()
lat = data['loc'].split(',')[0]
lon = data['loc'].split(',')[1]


def func_weather(city, weather_token):
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}'
    )
    data = r.json()
    print(data)


def func_weat():
    a = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_token}'
    )
    data = a.json()
    name = data['name']
    temp = data['main']['temp']
    print(f'{name}\n{temp}')
    return


# def weather():
#     result = func_weat()
#     print(func_weat())


if __name__ == '__main__':
    func_weat()
