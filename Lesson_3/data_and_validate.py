import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.wikipedia.org/')
url = driver.current_url
print(url)
assert url == 'https://www.wikipedia.org/', 'URL is not correct'

current_title = driver.title
print(current_title)
assert current_title == 'Wikipedia', 'Title is not correct'

print(driver.page_source)
time.sleep(2)

