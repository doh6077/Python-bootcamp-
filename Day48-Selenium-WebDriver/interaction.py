from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

number = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')


# Find by the link text 
all_portals = driver.find_element(By.LINK_TEXT, "Help desk")
# all_portals.click()


# ...existing code...

search = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "search"))
)
search.send_keys("Python")
search.send_keys(Keys.ENTER)

time.sleep(0.1)