from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(), options=options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# article_count.click()

# wildfires = driver.find_element(By.LINK_TEXT, "Wildfires")
# wildfires.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

f_name = driver.find_element(By.NAME, value="fName")
f_name.send_keys("Jovenson")
l_name = driver.find_element(By.NAME, "lName")
l_name.send_keys("Don")
email = driver.find_element(By.NAME, "email")
email.send_keys("joeydon21@gmail.com")
button = driver.find_element(By.TAG_NAME, "button")
button.click()

events_data = driver.find_elements(By.CSS_SELECTOR, ".event-widget li")
events_text = [event.text.split("\n") for event in events_data]


events = {f"{n}": {"time": events_text[n][0], "name": events_text[n][1]} for n in range(0, len(events_text))}
print(events)

# google_search_box = driver.find_element(By.ID, "APjFqb")
# google_search_box.send_keys("Automation")
# google_search_box.send_keys(Keys.RETURN)
# # driver.find_element(By.CLASS_NAME, "gNO89b")
#
time.sleep(2)
driver.quit()



# time.sleep(2)
# driver.close()

