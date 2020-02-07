from flask import Flask, render_template
from weather import weather_by_city
from news import get_python_news

app = Flask(__name__)


@app.route('/')
def hello():
    title = "Новости Python"
    weather = weather_by_city("Ryazan")
    news = get_python_news()
    return render_template('index.html', page_title=title, weather=weather, news=news)


if __name__ == '__main__':
    app.run()
