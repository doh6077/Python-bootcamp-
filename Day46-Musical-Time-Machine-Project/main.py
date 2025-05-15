from bs4 import BeautifulSoup
import requests
# filepath: main.py
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

load_dotenv()  # take environment variables from .env

auth = spotipy.SpotifyOAuth(client_id=os.getenv("CLIENT_ID"),
                    client_secret=os.getenv("CLIENT_SECRET"),
                    redirect_uri="http://example.com",
                    scope="playlist-modify-private")


# get access to the token 
token = auth.get_cached_token()
# print(token)
# sp = spotipy.Spotify(auth = os.getenv("SPOTIPY_ACCESS_TOKEN"))
sp = spotipy.Spotify(token['access_token'])
# user = sp.current_user()['display_name']

HTML_DOC = "https://www.billboard.com/charts/hot-100/"

# he main purpose of setting the User-Agent header is to make your request look like it’s coming from a real web browser instead of a script or bot
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
date = '2000-08-12'
# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")


response = requests.get(f'{HTML_DOC}/{date}', headers=headers)
print(response.status_code)
soup = BeautifulSoup(response.text, 'html.parser')

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
spotify_songs = [] 
urls = []
for song in song_names:
    result = sp.search(q='track:' + song + ' year:' + date.split('-')[0], type="track")
    try:
        track_uri = result['tracks']['items'][0]['uri']
        urls.append(track_uri)
    except (IndexError, KeyError):
        print(f"Track not found for: {song}")


user_id = sp.current_user()["id"]
playlists = sp.user_playlists(user_id)
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

# Add songs from step3 to the playlist 

sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist['id'], tracks=urls)