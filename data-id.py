from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

caps = DesiredCapabilities().CHROME
# caps["pageLoadStrategy"] = "normal"  #  Waits for full page load
caps["pageLoadStrategy"] = "eager"   # Do not wait for full page load

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(desired_capabilities=caps,  options=chrome_options)


driver.get("https://primewire.mx/watch-tv/watch-friends-online-39473.1611980")
modal = driver.find_element(By.CLASS_NAME,"text-close").click()
elem = driver.find_element(By.CLASS_NAME,"nav-link btn btn-sm btn-secondary eps-item active")
id = elem.get_attribute("data-id")
print(id)