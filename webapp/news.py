import requests
from bs4 import BeautifulSoup
from datetime import datetime
from webapp.model import db, News


def get_html(url):
    try:
        result = requests.get(url)
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


def get_python_news():
    html = get_html("https://www.python.org/blogs/")

    if not html:
        return False

    soup = BeautifulSoup(html, "html.parser")

    all_news = soup.find("ul", {"class": "list-recent-posts"}).findAll("li")
    for news in all_news:
        title = news.find("a").text
        url = news.find("a").get("href")
        published = news.find("time").text

        try:
            published = datetime.strptime(published, "%Y-%m-%d")
        except (ValueError):
            published = datetime.now()

        save_news(title=title, url=url, published=published)
