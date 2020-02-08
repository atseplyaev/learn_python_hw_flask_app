from flask import Flask, render_template
from webapp.weather import weather_by_city
from webapp.news import get_python_news
from webapp.model import db, News


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def hello():
        title = "Новости Python"
        weather = weather_by_city(app.config["WEATHER_DEFAULT_CITY"])
        news = News.query.order_by(News.published.desc()).all()
        return render_template('index.html', page_title=title, weather=weather, news=news)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
