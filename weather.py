import requests
from utils import get_param

def weather_by_city(city_name):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "units": "metric",
        "APPID": get_param("weather_api", "APPID")
    }
    result = requests.get(url, params=params)
    return result.json()
    # if 'main' in weather:
    #         if "temp" in weather['main']:
    #             return weather["main"]["temp"]
