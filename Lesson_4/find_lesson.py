import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# driver.get("https://www.freeconferencecall.com/ru/ru/login")
# driver.find_element('id', 'appleid-signin').click()
# time.sleep(5)

driver.get("https://testautomationpractice.blogspot.com") # Откроем тестовую страницу
ELEMENT = driver.find_element('id', "Wikipedia1_wikipedia-search-input")
# ELEMENT = driver.find_element('class name', "wikipedia-search-input")
print(ELEMENT)