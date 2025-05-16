from selenium import webdriver 
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

number = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')

print(number.text)