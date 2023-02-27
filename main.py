import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#add to PATH variable

DRIVER_PATH = r'/Users/sunny/Desktop/WebDev/SeleniumProject'
os.environ['PATH'] += DRIVER_PATH


driver=webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(10) #wait 3 seconds maximum.. move on if element is found before 3 seconds.
driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")

my_element = driver.find_element(By.ID, "downloadButton")
my_element.click()



WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "progress-label"),#element filtration
        'Complete!'#expected text
    )
)

progress_element=driver.find_element(By.CLASS_NAME, "progress-label")
print(f"{progress_element.text}")

second_element=driver.find_elements(By.CSS_SELECTOR,"button.ui-button")[2]
print("secondClick", second_element.text)
second_element.click()