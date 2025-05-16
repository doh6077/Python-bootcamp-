from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome()
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = "Dohee"
last_name ="Kim"
email_address = "doh6077@gmail.com"
first_name_form = driver.find_element(By.NAME, value='fName')
last_name_form = driver.find_element(By.NAME, value='lName')
email_address_form  = driver.find_element(By.NAME, value='email')


first_name_form.send_keys(first_name)
last_name_form.send_keys(last_name)
email_address_form.send_keys(email_address)
time.sleep(3)


button = driver.find_element(By.CSS_SELECTOR, value=".btn")
button.click()
time.sleep(3)