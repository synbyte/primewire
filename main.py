from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://primewire.mx")
query = input("search for..\n")
elem = driver.find_element(By.CLASS_NAME, "search-input")
elem.clear()
id = "11239"
elem.send_keys(query)
elem.send_keys(Keys.RETURN)
elem = driver.find_element(By.CLASS_NAME,"film-name").click()
elem = driver.find_element(By.CLASS_NAME,"active")
id = elem.get_attribute("data-id")
print(id)

elem.send_keys(Keys.RETURN)