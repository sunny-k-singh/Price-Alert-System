from Booking.booking import Booking
from selenium.webdriver.common.by import By
import time
import sys
# inst=Booking()
# inst.land_first_page()

if __name__=='__main__':

    destination=sys.argv[1]
    start_date=sys.argv[2]
    end_date=sys.argv[3]
    count=sys.argv[4]
    sort=sys.argv[5]

    # print(destination,start_date,end_date,count)
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
        bot.select_place_to_go(destination)
        try:
            bot.choose_date(start_date,end_date)
        except Exception as e:
            print("Choose date didn't work!!, Eception is : ",e)    
        try:
            bot.choose_people(count) 
        except Exception as e:
            print("Choose people didn't work!!, Exception is: ",e)       

        bot.sort_rooms(sort)    