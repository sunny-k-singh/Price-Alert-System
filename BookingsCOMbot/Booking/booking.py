from selenium import webdriver
import Booking.constants as const
from selenium.webdriver.common.by import By
import time
# from Booking.bookingFiltration import BookingFiltration



import os
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
#the drivers of Booking class will have extra methods on top of webdriver.Chrome
class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r'/Users/sunny/Desktop/WebDev/SeleniumProject',teardown=False):
        self.driver_path=driver_path
        os.environ["PATH"]+=self.driver_path
        self.teardown=teardown
        super(Booking, self).__init__(chrome_options=chrome_options)
        self.implicitly_wait(25)
        self.maximize_window()

    def land_first_page(self):
        self.get(const.BASE_URL)    

    def change_currency(self, currency=None):
        my_element = self.find_element(By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]')
        my_element.click()

        select_currency=self.find_elements(By.CSS_SELECTOR, 'div')
        for currency in select_currency:
            if currency.text == 'USD':
                currency.click()


    def select_place_to_go(self, place="Kolkata"):
        my_element=self.find_element(By.ID, ":Ra9:")
        my_element.clear()
        my_element.send_keys(place)
        time.sleep(4)
        my_element = self.find_element(By.CSS_SELECTOR, "li.a80e7dc237")
        print(my_element.text)

        action = webdriver.common.action_chains.ActionChains(self)
        action.move_to_element_with_offset(my_element, 5, 5)
        action.click()
        action.perform()
       
    def choose_date(self, start_date="2023-03-13", end_date="2023-03-16"):
        
        my_element = self.find_element(By.CSS_SELECTOR, f'span[data-date="{start_date}"]')
        my_element.click()
        my_element = self.find_element(By.CSS_SELECTOR, f'span[data-date="{end_date}"]')
        my_element.click()
        print("date chosen!")

    def choose_people(self,count=1):

        count=int(count)
        my_element = self.find_element(By.CSS_SELECTOR, 'button[data-testid="occupancy-config"]')
        my_element.click()
        my_element = self.find_elements(By.CSS_SELECTOR, "span.b9def0936d")[1]
        my_element.click()
        my_element = self.find_elements(By.CSS_SELECTOR, "span.b9def0936d")[2]

        for i in range(count-1):
            my_element.click()

        my_element = self.find_elements(By.CSS_SELECTOR, "span.e57ffa4eb5")[6]
        my_element.click()


    def sort_rooms(self,sort="price"): #price, class, class_and_price
        my_element = self.find_elements(By.CSS_SELECTOR, "span.e57ffa4eb5")[7]
        my_element.click()
        
        my_element = self.find_element(By.CSS_SELECTOR, f'button[data-id="{sort}"]')
        my_element.click()
            
    # def applyFilter(self):
    #    filter=BookingFiltration(driver=self)
    #    filter.sort_rooms(sort="")


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
