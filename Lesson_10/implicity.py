from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.get('https://demoqa.com/dynamic-properties')

VISIBLE_AFTER_WAIT = ('xpath', '//button[@id="visibleAfter"]')

driver.find_element(*VISIBLE_AFTER_WAIT).click()
