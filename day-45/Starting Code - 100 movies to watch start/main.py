import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
website = response.text
soup = BeautifulSoup(website, "html.parser")

headers = soup.find_all(name="h3")

movie_list = [title.getText() for title in headers]
movies = reversed(movie_list)

with open("move_list", "w", encoding="utf8") as data:
    for movie in movies:
        data.write(f"{movie}\n")


