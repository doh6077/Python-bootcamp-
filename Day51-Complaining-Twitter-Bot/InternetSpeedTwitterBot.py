from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep
from dotenv import load_dotenv
import os 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




class InternetSpeedTwitterBot:
    # init method or constructor
    def __init__(self):
        load_dotenv() 
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)

        self.speed_driver = driver
        self.twitter_driver = driver
        self.up = 0
        self.down = 0
        self.promissing_up = os.getenv('PROMISED_UP')
        self.promissing_down = os.getenv('PROMISED_DOWN')

    def get_internet_speed(self):
        url ="https://www.speedtest.net/"
        self.speed_driver.get(url)
        start_btn = self.speed_driver.find_element(By.CSS_SELECTOR, '.js-start-test')
        if start_btn != None:
            start_btn.click()
            print("Start button has been clicked")
            sleep(120)
            close_btn = self.speed_driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[8]/div/div/div[2]/a')
            
            if close_btn == None:
                print("close button can't be found")
                exit
            else:
                print("close button has been found")
                close_btn.click() 
            sleep(5)

            result_down = self.speed_driver.find_element(By.CLASS_NAME,'download-speed')
            self.down = result_down.text
            print(f"down: {self.down}")

            result_up = self.speed_driver.find_element(By.CLASS_NAME,'upload-speed')
            self.up = result_up.text
            print(f"up: {self.up}")

            self.speed_driver.quit()

        else:
            print("start button can't be found")
    
    def tweet_at_provider(self):
        load_dotenv() 
        url_twitter ="https://x.com/home"
        self.twitter_driver.get(url_twitter)
        sleep(5)
        username_input = self.twitter_driver.find_element(By.NAME, "text")
        user_name = os.getenv('TWITTER_USERNAME')
        print(f"this is user_name {user_name}")
        username_input.send_keys(user_name)
        next_btn = self.twitter_driver.find_element(
    By.CSS_SELECTOR,
    '.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-ywje51.r-184id4b.r-13qz1uu.r-2yi16.r-1qi8awa.r-3pj75a.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l'
)
        next_btn.click()
        sleep(5)
        password = self.twitter_driver.find_element(By.NAME, 'password')
        password.send_keys(os.getenv('TWITTER_PASSWORD'))

        signin_btn = self.twitter_driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div/span/span')
        signin_btn.click()
        sleep(10)
        body = f'Hey Internet Provider, why is my internet speed {self.down} down / {self.up} up when I pay for {self.promissing_down} / {self.promissing_up}'
        body_text = self.twitter_driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
        body_text.send_keys(body)

        # post button 
        post_btn = self.twitter_driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
        post_btn.click()

        self.twitter_driver.quit()
        


# Python day 16 -20 Lectures 

