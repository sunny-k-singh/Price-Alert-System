import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#add to PATH variable

DRIVER_PATH = r'/Users/sunny/Desktop/WebDev/SeleniumProject'
os.environ['PATH'] += DRIVER_PATH

driver=webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(10) #wait 3 seconds maximum.. move on if element is found before 3 seconds.
driver.get("https://www.calculator.net/")
my_element = driver.find_element(By.CSS_SELECTOR, 'span[onclick="r(5)"]')
# print(len(my_element)) #keys can be sent to fields and inputs
# my_element.send_keys(Keys.NUMPAD1, Keys.NUMPAD5) #sending 15
my_element.click()
my_element = driver.find_element(By.CSS_SELECTOR, 'span[onclick="r(\'*\')"]')
my_element.click()
my_element = driver.find_element(By.CSS_SELECTOR, 'span[onclick="r(8)"]')
my_element.click()
my_element = driver.find_element(By.CSS_SELECTOR, 'span[onclick="r(\'=\')"]')
my_element.click()

amortization=driver.find_element(By.ID, "calcSearchTerm")
amortization.send_keys("Amortization")
search=driver.find_elements(By.CSS_SELECTOR, 'a')[1]
search.click()

#FOR CSS SELECTOR PATTERNS, https://www.w3schools.com/cssref/css_selectors.php