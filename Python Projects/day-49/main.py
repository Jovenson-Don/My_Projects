import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

EMAIL = "jovensondon@yahoo.com"
PASSWORD = os.environ.get("LINKEDIN_PASSWORD")

options = webdriver.ChromeOptions()
options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(service=Service(), options=options)
driver.get(url="https://www.linkedin.com/jobs/search/"
               "?currentJobId=3681464751&distance=25&f"
               "_AL=true&geoId=102380872&keywords=Python%20Developer&refresh=true")

# Click Sign In
time.sleep(3)
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

# Enter credentials
username = driver.find_element(By.NAME, "session_key")
username.send_keys(EMAIL)
password = driver.find_element(By.NAME, "session_password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

# You may be presented with a CAPTCHA - Solve the Puzzle Manually
input("Press 'Enter' when you have solved the Captcha: ")

# Locate apply button
time.sleep(5)
apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button")
apply_button.click()

next_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
next_button.click()

review_button = driver.find_elements(by=By.CSS_SELECTOR, value="footer button")
review_button[1].click()

submit_button = driver.find_elements(by=By.CSS_SELECTOR, value="footer button")
submit_button[1].click()

