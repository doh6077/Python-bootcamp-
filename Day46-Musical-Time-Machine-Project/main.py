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
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")


response = requests.get(f'{HTML_DOC}/{date}', headers=headers)
print(response.status_code)
soup = BeautifulSoup(response.text, 'html.parser')

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
spotify_songs = [] 
urls = []
print(date.split('-')[0])
for song in song_names:
    result = sp.search(q='track:'+ song +'year:'+ date.split('-')[0], type="track")
    pprint.pprint(result['tracks']['href'])
    urls.append(result)

# print(urls)
# 1. 스포티파이 문서를 보고, 1단계(빌보드 탑 100 스크래핑)에서 찾은 곡 목록에 해당하는 스포티파이 노래 URI 목록을 만드세요.

# 힌트 1: 특정 연도에 나온 곡명으로 좁히기 위해 쿼리 형식은 ‘track: {name} year: {YYYY}’을 사용합니다.

# 힌트 2: 스포티파이에 곡이 없을 수도 있으니, 예외 처리를 통해 해당 곡들을 건너뛰세요.

# 힌트 3: pprint()를 사용해 결과를 보기 좋게 출력하세요. https://docs.python.org/3/library/pprint.html


# tracks(tracks, market=None)
# returns a list of tracks given a list of track IDs, URIs, or URLs

# Parameters:
# tracks - a list of spotify URIs, URLs or IDs. Maximum: 50 IDs.
# market - an ISO 3166-1 alpha-2 country code.