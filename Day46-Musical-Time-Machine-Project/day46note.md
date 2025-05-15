## BeautifulSoup

Beautiful Soup is a Python library for pulling data out of HTML and XML files.

```python
from bs4 import BeautifulSoup
import requests
import lxml

with open("website.html", encoding='utf-8') as file:
    contents = file.read()

# it enables us to access the HTML
soup = BeautifulSoup(contents, "lxml")

print(soup.title.string)
```

- If we don’t have access to the API, we can use BeautifulSoup to get the data from the page.

```python
all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags: 
    print(tag.get("href"))
```

---

```python
# find specific values which have attributes
heading = soup.find(name="h1", id="name")
section_heading = soup.find(name="h3", class_="heading")
```

### select_one

- It gives us the first item of matching.

```python
class_is_heading = soup.find_all(class_="heading")

h3_heading = soup.find_all("h3", class_="heading")

name = soup.select_one("#name")

headings = soup.select(".heading") 
```

---

## Live Website

```python
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

print(response.text)
```

- We can get data from the website using the requests library.

### get_text()

- If you only want the human-readable text inside a document or tag, you can use the `get_text()` method. It returns all the text in a document.

### function find_all()

```python
all_anchor_tags = soup.find_all(name="a")
```

- It will return all matching elements.

### Other examples of finding

```python
# it enables us to access the HTML
soup = BeautifulSoup(contents, "lxml")

# print(soup.title.string)

all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")  # prints the value of h1 with id="name"

# <h3 class="heading"> Books and Teaching </h3>
# checks if the attribute is heading
section_heading = soup.find(name="h3", class_="heading") 
print(section_heading.get())
```

### Complex cases

```python
company_url = soup.select_one(selector="p a")
# looks for an <a> tag inside a <p> tag

# we can use CSS selectors to get any item on the page
name = soup.select_one("#name")

headings = soup.select(".heading")
```

```python
article_tag = soup.find(name="a", class_="storylink")
article_text = article_tag.getText()
article_link = article_tag.get("href")
article_upvote = soup.find(name="span", class_="score").getText()
```

### Movie Project

```python
from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

yc_web_page = response.text
titleList = []
soup = BeautifulSoup(yc_web_page, "html.parser")
all_titles = soup.find_all(name="h3", class_="title")
for title in all_titles:
    titleList.append(title.string)

print(titleList)
```

```python
from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
```