from bs4 import BeautifulSoup
from datetime import date
import requests

year, month, day = map(int, input("Enter date (YYY MM DD): ").split())
my_date = date(year, month, day)

response = requests.get(f"https://www.billboard.com/charts/hot-100/{my_date}/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    song_elements = soup.find_all('h3', id='title-of-a-story',class_='c-title')
    song_names = [song.text.strip() for song in song_elements if song.text.strip() not in ('Songwriter(s):','Producer(s):','Imprint/Promotion Label:')]
    with open('song.txt','w',encoding='utf-8') as file:
        file.write('\n'.join(song_names))
        print("songs names have been saved to song.txt")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")