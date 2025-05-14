from bs4 import BeautifulSoup
import requests
# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')

# print(soup.prettify())


# lists = soup.find_all('li')
# list_text = []
# for list in lists:
#     list_text.append(list.get_text())

# soup.select_one()

response = requests.get('https://news.ycombinator.com/news')

web_page = response.text


soup = BeautifulSoup(web_page, 'html.parser')
print(soup.prettify())