from selenium import webdriver 
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome()
driver.get("https://www.python.org/")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar}.{price_cents}")


# This is useful to fill up the form ( name, or id By.ID)
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.tag_name)
# find css selector 
# - in case if there is no id, class (specific)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link)

# when there is no unique class or id.
# xpath 
# driver.find_element(By.XPATH, value='')

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time" : event_times[n].text,
        "name" : event_names[n].text
    }

print(events)
# print(events[0])
# events = events.text.split('\n')
# print(events)
# event_dict = {}
# for i in range(len(events)):
#     print(events[i].text)
#     if i % 2 == 0:
#         event_dict[events[i].text] = ""
#     else:
#         event_dict[i-1] = events[i].text
# print(event_dict)


# driver.close()
driver.quit() # quit entire program 