import requests
from utils import get_param


def weather_by_city(city_name: str):
    """
    Возвращает данные о погоде в заданом городе.
    :param city_name: Название города.
    :return dict: Данные о погоде.
    """
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "units": "metric",
        "APPID": get_param("weather_api", "APPID")
    }
    try:
        result = requests.get(url, params=params)
        result.raise_for_status()
        return result.json()

    except (requests.RequestException, ValueError):
        return False
