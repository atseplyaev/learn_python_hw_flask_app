from webapp.utils import get_param
import os
from  datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "..", "webapp.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False
WEATHER_DEFAULT_CITY = "Ryazan"
WEATHER_API_KEY = get_param("weather_api", "APPID")
SECRET_KEY = os.urandom(24)
REMEMBER_COOKIE_DURATION = timedelta(days=5)
