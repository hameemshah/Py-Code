from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')
print(soup.select('.titleline a').get('href'))
print(soup.find(class_='score', name='span').getText())