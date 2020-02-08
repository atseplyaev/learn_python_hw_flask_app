from webapp.utils import get_param
import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "..", "webapp.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False
WEATHER_DEFAULT_CITY = "Ryazan"
WEATHER_API_KEY = get_param("weather_api", "APPID")
