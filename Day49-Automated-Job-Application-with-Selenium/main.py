from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
import os 
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from selenium.common.exceptions import NoSuchElementException
load_dotenv()

url ="https://www.linkedin.com/jobs/collections/easy-apply/?currentJobId=4220162457&discover=recommended&discoveryOrigin=JOBS_HOME_JYMBII"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
driver.implicitly_wait(time_to_wait=10) 

# sign_in = driver.find_element(By.CLASS_NAME, 'nsm7Bb-HzV7m-LgbsSe-BPrWId')
# sign_in.click()
time.sleep(5)

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


# input email and password 
email = driver.find_element(By.ID,"username")
password = driver.find_element(By.ID,"password")

email.send_keys(EMAIL)
# email.send_keys(Keys.ENTER)

password.send_keys(PASSWORD)
# password.send_keys(Keys.ENTER)

# driver.quit()

# find button for sign in 
time.sleep(5)
sign_in = driver.find_element(By.CLASS_NAME, 'from__button--floating')
print(sign_in.text)
sign_in.click()
time.sleep(5)

# Step 3: Save job and follow the company 

save_btn = driver.find_element(By.CLASS_NAME,'jobs-save-button__text')
save_btn.click()
follow_btn = driver.find_element(By.CSS_SELECTOR, ".artdeco-button.artdeco-button--secondary.ml5")
if follow_btn != None:
    print("follow button has been found")
# follow_btn.click()


# Step 4: do the step3 for multiple jobs 
jobs = driver.find_elements(By.CSS_SELECTOR,'.job-card-list__title--link')
for job in jobs: 
    print(job)
    job.click()
    print(f"job {job.text} has been clicked")
    time.sleep(2)

driver.quit()
