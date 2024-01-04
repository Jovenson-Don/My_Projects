import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(service=Service(), options=options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

cookie_counter = 0
while time.time():
    cookie.click()
    cookie_counter += 1






