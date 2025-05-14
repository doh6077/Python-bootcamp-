from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

print(soup.prettify())


lists = soup.find_all('li')
list_text = []
for list in lists:
    list_text.append(list.get_text())

soup.select_one()