from Booking.booking import Booking
from selenium.webdriver.common.by import By
import time
# inst=Booking()
# inst.land_first_page()

with Booking() as bot:
    bot.land_first_page() #after python crosses this indentation in with
    #it will create some teardown action. The __exit__ method will be called
    #print("Exiting....")
    try:
        my_element = bot.find_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss sign in information."]')
        my_element.click()
        print("Popp up closed!!!")
        time.sleep(2)
    except Exception:
        print("This didn't work!!!!!")

    # bot.change_currency()
    time.sleep(2)    
    bot.select_place_to_go("Mumbai")
    try:
        bot.choose_date()
    except Exception as e:
        print("Choose date didn't work!!, Eception is : ",e)    
    try:
        bot.choose_people(count=3) 
    except Exception as e:
        print("Choose people didn't work!!, Exception is: ",e)       

    bot.sort_rooms(sort="price")    