from tech_news.database import find_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    news = find_news()
    list_news = []
    for new in news:
        if (title.lower() in new['title'].lower()):
            list_news.append((new['title'], new['url']))
    return list_news


# Requisito 8
def search_by_date(date):
    try:
        news = find_news()
        list_news = []
        date_format = (
            datetime
            .strptime(date, '%Y-%m-%d').strftime('%d-%m-%Y').replace('-', '/')
        )
        for new in news:
            if (date_format.lower() in new['timestamp'].lower()):
                list_news.append((new['title'], new['url']))
        return list_news
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 9
def search_by_category(category):
    news = find_news()
    list_news = []
    for new in news:
        if (category.lower() in new['category'].lower()):
            list_news.append((new['title'], new['url']))
    return list_news
