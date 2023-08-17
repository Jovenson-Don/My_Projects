import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.python.org/")


elements = driver.find_elements(By.CSS_SELECTOR, ".event-widget li")

for tag in elements:
    print(tag.text)



# google_search_box = driver.find_element(By.ID, "APjFqb")
# google_search_box.send_keys("Automation")
# google_search_box.send_keys(Keys.RETURN)
# # driver.find_element(By.CLASS_NAME, "gNO89b")
#
# time.sleep(2)
# driver.quit()
#
#
