
# 1단계 - BeautifulSoup으로 상품 가격 스크래핑하기
# 연습 페이지에서 BeautifulSoup 사용하기


# 라이브 웹사이트는 많이 바뀝니다. 실제 웹사이트로 이동하기 전에 아마존 페이지의 복제본에서 프로젝트의 첫 번째 버전을 작동시켜 보겠습니다. 여기를 살펴보세요:



# https://appbrewery.github.io/instant_pot/



# 1. BeautifulSoup을 사용하여 품목의 가격을 부동 소수점 숫자로 가져와서 인쇄합니다. 이렇게 결과물이 나와야합니다:


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

response = requests.get('https://appbrewery.github.io/instant_pot/')

web_page = response.text


soup = BeautifulSoup(web_page, 'html.parser')

price = soup.find(class_="a-offscreen").get_text().split('$')[1]
price = float(price)