import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = 'eager'
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--ignore-certificate-errors")
# chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument('--disable-cash')

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
# driver.set_window_size(1920, 1080)

start = time.time()
driver.get('https://whatismyipaddress.com/')
end = time.time()
print(end - start)
