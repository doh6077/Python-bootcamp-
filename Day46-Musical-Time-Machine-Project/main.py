from bs4 import BeautifulSoup
import requests

HTML_DOC = "https://www.billboard.com/charts/hot-100/"

# he main purpose of setting the User-Agent header is to make your request look like it’s coming from a real web browser instead of a script or bot
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")


response = requests.get(f'{HTML_DOC}/{date}', headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

song_names_spans = soup.select("li ul li h3")
print(song_names_spans)
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)