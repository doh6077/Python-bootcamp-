from InternetSpeedTwitterBot import InternetSpeedTwitterBot as Bot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep
from dotenv import load_dotenv
import os 
from dotenv import load_dotenv
load_dotenv()
print("TWITTER_USERNAME:", os.getenv('TWITTER_USERNAME'))
bot = Bot()
# bot.get_internet_speed()
bot.tweet_at_provider()