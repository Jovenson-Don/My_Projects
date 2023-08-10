import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
website = response.text
soup = BeautifulSoup(website, "html.parser")

headers = soup.find_all(name="h3")
print(headers)

# for title in headers:
#     print(title.getText())


