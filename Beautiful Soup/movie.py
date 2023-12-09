from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.find_all('h3', class_='listicleItem_listicle-item__title__hW_Kn')
movies = [title.getText() for title in titles]
print(movies[::-1])
with open('title.txt', 'w') as file:
    for movie in movies[::-1]:
        file.write(f"{movie}\n")