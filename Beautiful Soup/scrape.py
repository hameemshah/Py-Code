import bs4
with open("index.html", 'r') as file:
    data = file.read()
    soup = bs4.BeautifulSoup(data, 'html.parser')
    link = soup.select('.top')
    print(link)