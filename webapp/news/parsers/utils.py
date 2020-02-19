import requests
from webapp.news.models import News
from webapp.db import db


def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    }
    try:
        result = requests.get(url, headers=headers)
        result.raise_for_status()
        return result.text

    except (requests.RequestException, ValueError):
        return False


def save_news(title, url, published):
    news_exists = News.query.filter(News.url == url).count()
    if not news_exists:
        new = News(title=title, url=url, published=published)
        db.session.add(new)
        db.session.commit()

