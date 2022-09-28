from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
site = response.text


soup = BeautifulSoup(site,"html.parser")
articles = soup.find_all(name='span', class_='titleline')

titles = []
links = []


for article in articles:
    titles.append(article.getText())
    links.append(article.next.get('href'))

article_score = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

max = max(article_score)
index = article_score.index(max)

print(f"{titles[index]} - {links[index]}")
