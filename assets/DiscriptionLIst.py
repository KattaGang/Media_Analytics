from GoogleNews import GoogleNews
from newspaper import Article
import pandas as pd
import requests
from bs4 import BeautifulSoup

googlenews=GoogleNews(start='01/01/2022',end='05/01/2023')
googlenews.search('Twiter')
result=googlenews.result()
df=pd.DataFrame(result)
LIST = []
i = 0
for element in df.link:
    Dir = {}
    url = element
    r = requests.get(url)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    title = soup.title
    Dir['Title'] = title.get_text()
    Dir['Link'] = url
    Dir['Date'] = df.date[i]
    i = i+1
    Dir['Discription'] = soup.get_text()
    # print(soup.get_text())
    LIST.append(Dir)
print(LIST)