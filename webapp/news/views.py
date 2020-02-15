from flask import Blueprint, render_template, current_app
from webapp.weather import weather_by_city
from .models import News
bp = Blueprint("news", __name__, url_prefix="/")


@bp.route("/")
def index():
    title = "Новости Python"

    weather = weather_by_city(current_app.config["WEATHER_DEFAULT_CITY"])
    news = News.query.order_by(News.published.desc()).all()
    return render_template("news/index.html", page_title=title, weather=weather, news=news)
