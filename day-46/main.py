import os
import bs4
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests

URL = "https://www.billboard.com/charts/hot-100/"

SPOTIFY_REDIRECT_URI = "http://example.com"
SPOTIFY_ID = os.environ.get("spotify_id")
SPOTIFY_SECRET = os.environ.get("spotify_secret")
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_ID,
                                               client_secret=SPOTIFY_SECRET,
                                               redirect_uri=SPOTIFY_REDIRECT_URI,
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               username="jovensondon")
                     )
user_id = sp.current_user()["id"]

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(URL + date)
website = response.text

soup = bs4.BeautifulSoup(website, "html.parser")
song_titles = soup.find_all(name="h3", class_="a-no-trucate")

song_title = [title.get_text().strip() for title in song_titles]

playlist = sp.user_playlist_create(user=user_id,
                                   name=f"{date} Billboard 100",
                                   public=False,
                                   description=f"Top 100 songs on {date}")

song_url = []
year = date.split("-")[0]
for song in song_title:
    results = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        url = results["tracks"]["items"][0]["external_urls"]["spotify"]
        song_url.append(url)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

sp.playlist_add_items(playlist_id=playlist["id"], items=song_url)
