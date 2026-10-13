from pydoc import text

from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/news"
get_requests = requests.get(url)
web = get_requests.text
soup = BeautifulSoup(web, 'html.parser')
articles = soup.find_all(name="span", class_="titleline")
articles_text = []
articles_links = []
for article in articles:
    text = article.getText()
    articles_text.append(text)
    link1 = article.find(name="a")
    link = link1.get("href")
    articles_links.append(link)


article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(articles_text)
# print(articles_links)
# print(article_upvote)

largest_vote = max(article_upvote)
if largest_vote in article_upvote:
    index_value = article_upvote.index(largest_vote)
    print(article_upvote[index_value])
    print(articles_text[index_value])
    print(articles_links[index_value])
# largest_article = articles_text.index(articles_text,largest_vote)
# print(largest_article)



