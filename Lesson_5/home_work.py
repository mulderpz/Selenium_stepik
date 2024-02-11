import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#Задание 1:

#Заполнить все текстовые поля данными (почистить поля перед заполнением).
#Проверить, что данные действительно введены, используя get_attribute() и assert.
#Страница для выполнения задания: https://demoqa.com/text-box

driver.get('https://demoqa.com/text-box')
driver.maximize_window()


full_name = driver.find_element('xpath','//input[@placeholder = "Full Name"]')
full_name.clear()
# Проверяем, что в поле пусто
assert full_name.get_attribute("value") == ""
full_name.send_keys('Игорь')
time.sleep(2)





#
# # Записываем значение поля в переменную
# email_field_value = email_field.get_attribute("value")
#
# # Проверяем, что в поле email содержится введенный логин
# assert "example@yandex.ru" in email_field_value

