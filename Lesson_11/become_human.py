import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
# options.add_argument('--headless')
options.add_argument('--window-size=1920,1080')
options.add_argument('disable-blink-features=AutomationControlled')
options.add_argument("--ignore-certificate-errors")
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.1')

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 5, poll_frequency=1)

# driver.get('https://dzen.ru')
# driver.save_screenshot('123.png')

driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')


# driver.get('https://whatismyipaddress.com/')
time.sleep(5)
driver.save_screenshot('123.png')
# wait.until(EC.title_is('What Is My IP Address - See Your Public Address - IPv4 & IPv6'))
# time.sleep(5)