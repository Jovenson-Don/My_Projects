import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

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

# Locate all job listing
locate_all_jobs = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
print(len(locate_all_jobs))
# Loop through each listing
for job in locate_all_jobs:
    job.click()
    time.sleep(2)
    # Click Easy Apply Button
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, value=".jobs-apply-button")
        apply_button.click()
    # Click Next Button
        next_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        next_button.click()
    # Check for another Next Button
        another_next_button = driver.find_elements(By.CSS_SELECTOR, value="footer button")
    # If True close box and continue Loop
        if another_next_button[1].text == "Next":
            x_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/button")
            time.sleep(1)
            x_button.click()
            discard_button = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div[3]/button[1]")
            time.sleep(1)
            discard_button.click()
    # Submit Application
        else:
            review_button = driver.find_elements(by=By.CSS_SELECTOR, value="footer button")
            review_button[1].click()

            submit_button = driver.find_elements(by=By.CSS_SELECTOR, value="footer button")
            submit_button[1].click()
    # Skip jobs already applied too
    except NoSuchElementException:
        print("No element found. Skipping.")
