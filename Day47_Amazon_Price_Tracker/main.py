
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
from smtplib import SMTP
import os 

URL = 'https://appbrewery.github.io/instant_pot/'
response = requests.get(URL)

web_page = response.text


soup = BeautifulSoup(web_page, 'html.parser')

price = soup.find(class_="a-offscreen").get_text().split('$')[1]
price = float(price)


load_dotenv() # take environment variables from .env 

email = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")

s = SMTP(os.getenv("SMTP_ADDRESS"))

if price < 100:
    s.starttls()
    # Authentication
    s.login(email, password)
    # message to be sent
    message = f"The price has dropped! Purchase link: {URL} | Current price: ${price}"
    # sending the mail
    s.sendmail(email,email,message)
    # terminating the session
    s.quit()
else:
    print("The price is not enough low")