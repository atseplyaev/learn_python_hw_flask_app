from flask import Flask
from weather import weather_by_city

app = Flask(__name__)


@app.route('/')
def hello():
    weather = weather_by_city("Ryazan")
    if weather:
        return f"Сейчас {weather['main']['temp']}, ощущается как {weather['main']['feels_like']}"
    else:
        return "Прогноз погоды сейчас недоступен"


if __name__ == '__main__':
    app.run()
