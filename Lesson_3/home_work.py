import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://vk.com')
vk_title = driver.title
url = driver.current_url
print(vk_title)
print(url)

driver.get('https://www.ya.ru')
ya_title = driver.title
print(ya_title)
driver.back()
assert url == 'https://vk.com/', 'Ты попал, но не туда куда надо'
driver.refresh()
print(driver.current_url)
driver.forward()
print(driver.current_url)

