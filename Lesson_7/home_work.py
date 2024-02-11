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
def check_attr(el, a):
    el.clear()
    assert el.get_attribute("value") == ""
    el.send_keys(a)
    time.sleep(2)

email = driver.find_element('xpath','//input[@placeholder = "Full Name"]')
check_attr(email, 'Игорь')

email = driver.find_element('xpath','//input[@placeholder = "name@example.com"]')
check_attr(email, 'email@mail.ru')

current_address = driver.find_element('xpath','//textarea[@placeholder = "Current Address"]')
check_attr(current_address, '1213sdfwr32')

permanent_address = driver.find_element('xpath','//textarea[@id = "permanentAddress"]')
check_attr(permanent_address, '12313ljkjk')


# Задание 2:
#
# Прокликать все ссылки со статус-кодами на странице, используя алгоритм перебора элементов.
# После каждого клика возвращаться на стартовую страницу.
# Страница для выполнения задания: http://the-internet.herokuapp.com/status_codes

driver.get('http://the-internet.herokuapp.com/status_codes')
driver.maximize_window()
for code in ['200', '301', '404', '500']:
    driver.find_element('xpath', f'//a[@href = "status_codes/{code}"]').click()
    time.sleep(2)
    driver.back()


# button_200 = driver.find_element('xpath', '//a[@href = "status_codes/200"]')
# button_200.click()
# time.sleep(2)
# driver.back()
#
# button_301 = driver.find_element('xpath', '//a[@href = "status_codes/301"]')
# button_301.click()
# time.sleep(2)
# driver.back()
#
# button_404 = driver.find_element('xpath', '//a[@href = "status_codes/404"]')
# button_404.click()
# time.sleep(2)
# driver.back()
#
# button_500 = driver.find_element('xpath', '//a[@href = "status_codes/500"]')
# button_500.click()
# time.sleep(2)
# driver.back()

