import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Задание 1. Загрузить любой файл в 'Choose File'.
# Страница для выполнения задания: https://demoqa.com/upload-download
chrome_options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://demoqa.com/upload-download')
time.sleep(3)
upload_field = (driver.find_element('xpath', '//input[@type="file"]'))
upload_field.send_keys(f'{os.getcwd()}\downloads\Pamukkale.jpg')
time.sleep(3)

# Задание 2. С помощью цикла for скачать все файлы в папку lesson_6/downloads.
# Страница для выполнения задания: http://the-internet.herokuapp.com/download
chrome_options = webdriver.ChromeOptions()
prefs = {
    'download.default_directory': f'{os.getcwd()}\downloads',
}
chrome_options.add_experimental_option('prefs', prefs)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://the-internet.herokuapp.com/download')
elements = driver.find_elements('xpath', '//a')
for el in elements[1:]:
    el.click()
