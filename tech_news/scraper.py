import time
import requests
import parsel


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(
            url,
            headers={"user-agent": "Fake user-agent"},
            timeout=3
        )
        if response.status_code == 200:
            return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = parsel.Selector(html_content)
    url_selector = []
    for urlSelector in selector.css('.entry-header h2 a::attr(href)'):
        url = urlSelector.get()
        if url not in url_selector:
            url_selector.append(url)
    if url_selector:
        return url_selector
    return []


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    url_selector = []
    for urlSelector in selector.css('.navigation a::attr(href)'):
        url = urlSelector.get()
        if url not in url_selector:
            url_selector.append(url)
    if url_selector:
        return url_selector[-2]
    return None


# Requisito 4
def scrape_news(html_content):
    selector = parsel.Selector(html_content)
    info = {
        'url': selector.css('link[rel="canonical"]::attr(href)').get(),
        'title': selector.css('h1.entry-title::text').get().strip(),
        'timestamp': selector.css('li.meta-date::text').get(),
        'writer': selector.css('span.author a::text').get(),
        'reading_time': int(selector.css(
            'li.meta-reading-time::text'
        ).get().split()[0]),
        'summary': selector.css('.entry-content p').xpath(
            'string()'
        ).get().strip(),
        'category': selector.css('span.label::text').get(),
    }
    return info


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
