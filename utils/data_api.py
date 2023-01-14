from newsapi import NewsApiClient
from bs4 import BeautifulSoup
import requests


API_KEY = 'd83a0fb9e3104414a3693c6c4fdab735'


# Init
newsapi = NewsApiClient(api_key=API_KEY)


def getData(company_name):
    all_articles = newsapi.get_everything(q=company_name)
    articles = all_articles['articles'][:10]
    
    for article in articles:
        url = article['url']
        respones = requests.get(url)
        soup = BeautifulSoup(respones.content, 'html.parser')
        article.setdefault('title', 'title')
        article.setdefault('description', 'description')
        article.setdefault('url', 'https://datatofish.com/get-previous-current-and-next-day-system-dates-in-python/')
        article.setdefault('date', '2003-07-21')
        
        article['description'] = soup.get_text().replace('\n','')
    return articles


# # /v2/top-headlines/sources
# sources = newsapi.get_sources()


if __name__=='__main__':
    art = getData('exxon-mobile')
    print(art)
    art = art[0]
    print(len(art['description']))
    print(art['description'])