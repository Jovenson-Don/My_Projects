from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(service=Service(), options=options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

language = driver.find_element(By.ID, "promptAnchor")
print(language.text)
language.click()

cookie = driver.find_element(By.ID, "cookies")
cookie.click()
