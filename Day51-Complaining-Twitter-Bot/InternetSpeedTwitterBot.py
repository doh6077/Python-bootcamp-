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
    def __init__(self, speed_driver, twitter_driver, down, up):
        load_dotenv() 
        self.speed_driver = speed_driver
        self.twitter_driver = twitter_driver
        self.up = up
        self.down = down 
        self.promissing_up = os.getenv('PROMISED_UP')
        self.promissing_down = os.getenv('PROMISED_DOWN')

    def get_internet_speed(self):
        start_btn = self.speed_driver.find_element(By.CSS_SELECTOR, '.js-start-test')
        if start_btn != None:
            start_btn.click()
            print("Start button has been clicked")
            sleep(120)
            close_btn = self.speed_driver.find_element(By.CLASS_NAME,'close-btn')
            
            if close_btn == None:
                print("close button can't be found")
                exit
            else:
                print("close button has been found")
                close_btn.click() 
            sleep(5)

            result_down = self.speed_driver.find_element(By.CLASS_NAME,'download-speed')
            self.down = result_down.text()
            print(f"down: {self.down}")

            result_up = self.speed_driver.find_element(By.CLASS_NAME,'upload-speed')
            self.up = result_up.text()
            print(f"up: {self.up}")

            self.drive.quit()

        else:
            print("start button can't be found")
    
    def tweet_at_provider(self):
        body = f'Hey Internet Provider, why is my internet speed {self.down} down / {self.up} up when I pay for {self.promissing_down} / {self.promissing_up}'
        self.twitter_driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
        self.twitter_driver.send_keys('hi')
        print("hi")

        


# Python day 16 -20 Lectures 

