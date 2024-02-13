from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get('https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver')
# Кликнуть на кнопку “Change Text to Selenium Webdriver” и дождаться изменения текста элемента рядом
change_text_button = ('xpath', '//button[@id="populate-text"]')
selenium_text = ('xpath', '//h2[text()="Selenium Webdriver"]')
driver.find_element(*change_text_button).click()
wait.until(EC.text_to_be_present_in_element(selenium_text, "Selenium Webdriver"))

# Кликнуть на кнопку “Display button after 10 seconds” и дождаться появления кнопки “Enabled”
display_button = ('xpath', '//button[@id="display-other-button"]')
button = ('xpath', '//button[@id="hidden"]')
driver.find_element(*display_button).click()
wait.until(EC.visibility_of_element_located(button))

# Кликнуть на кнопку “Enable button after 10 seconds" и дождаться кликабельности кнопки “Button”
enable_button = ('xpath', '//button[@id="enable-button"]')
button = ('xpath', '//button[@id="disable"]')
driver.find_element(*enable_button).click()
wait.until(EC.element_to_be_clickable(button))

# Кликнуть на кнопку “Click me, to Open an alert after 5 seconds” и дождаться открытия алерта
alert_button = ('xpath', '//button[@class="btn btn-success"]')
driver.find_element(*alert_button).click()
wait.until(EC.alert_is_present())