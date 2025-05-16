
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
from smtplib import SMTP
import os 
import requests 

URL = 'https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1'
response = requests.get(URL, headers={    "Accept-Language": "en-US,en;q=0.9,it-IT;q=0.8,it;q=0.7,fr-CA;q=0.6,fr;q=0.5,es-MX;q=0.4,es;q=0.3,ko;q=0.2",
                                                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"})

web_page = response.text


soup = BeautifulSoup(web_page, 'html.parser')
price = soup.find(class_="a-offscreen").get_text().split('$')[1]
price = float(price)


load_dotenv() # take environment variables from .env 

email = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD", 587)
s = SMTP("smtp.gmail.com", port=587)

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