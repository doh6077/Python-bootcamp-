from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
from selenium_stealth import stealth


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_agent='user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
chrome_options.add_argument(user_agent)
driver = webdriver.Chrome(options=chrome_options)
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
)
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.implicitly_wait(time_to_wait=10)  

language = driver.find_element(By.ID, value='langSelect-EN')
language.click()
time.sleep(20)
btn = driver.find_element(By.ID, value="bigCookie")
result = True
time.sleep(5)
# while result:    
#     btn.click()

driver.quit()