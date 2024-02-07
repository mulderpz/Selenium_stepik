import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://hyperskill.org/tracks")
driver.maximize_window()

time.sleep(5)

# print(driver.find_elements('class name', 'nav-link'))
# print(len(driver.find_elements('class name', 'nav-link')))
driver.find_elements('class name', 'nav-link')[2].click()

time.sleep(5)