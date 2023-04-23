from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_categories():
    news = find_news()
    list_category = []
    for new in news:
        list_category.append(new['category'])
    top_categories = Counter(sorted(list_category)).most_common(5)
    list_top_category = []

    for category in top_categories:
        list_top_category.append(category[0])

    return list_top_category
