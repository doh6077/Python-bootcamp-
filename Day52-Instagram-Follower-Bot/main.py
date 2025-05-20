
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep
from dotenv import load_dotenv
import os 
from selenium.webdriver.common.by import By

load_dotenv()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
# Follow individual account 
USER_NAME = os.getenv('USERNAME_INSTAGRAM')
PASSWORD = os.getenv('PASSWORD')

driver.get("https://www.instagram.com/")

sleep(2)

user_name = driver.find_element(By.NAME, value='username')
user_name.send_keys(USER_NAME)

password = driver.find_element(By.NAME, value='password')
password.send_keys(PASSWORD)


login_btn = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button/div')
login_btn.click()

sleep(5)

