from InternetSpeedTwitterBot import InternetSpeedTwitterBot as Bot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep
from dotenv import load_dotenv
import os 
from dotenv import load_dotenv

load_dotenv()

up = os.getenv('PROMISED_UP')
down = os.getenv('PROMISED_DOWN')


# step1 : check the speed 
url ="https://www.speedtest.net/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# step 4: set up twitter driver 
url_twitter ="https://x.com/home"
driver_twitter = webdriver.Chrome(options=chrome_options)
driver_twitter.get(url_twitter)
bot = Bot(driver, driver_twitter, down, up)
bot.get_internet_speed()
bot.tweet_at_provider()