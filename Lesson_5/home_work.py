import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

time.sleep(3)
# Найти иконку Wikipedia по имени класса
print(driver.find_element('class name', 'wikipedia-icon'))
driver.find_element('class name', 'wikipedia-icon').click()
time.sleep(3)

# Найти поле ввода Wikipedia по id
print(driver.find_element('id', 'Wikipedia1_wikipedia-search-input'))

# Найти кнопку поиска Wikipedia по классу
print(driver.find_element('class name', 'wikipedia-search-button'))

#Найти любой другой элемент на странице по тегу
print(driver.find_elements("tag name", "table"))
