import csv

import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
real = response.text
soup = BeautifulSoup(real, "html.parser")
# Write your code below this line 👇

all_movies = soup.find_all(name="h3", class_="title")
movie_titles = (movie.getText() for movie in all_movies)

movies = list(movie_titles)[::-1]

with open("movies.txt", mode="w", encoding="UTF-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")
