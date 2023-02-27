# Bookings.com price alert system

- This application is designed to schedule a job for a bot that goes through [Booking.com](https://www.booking.com) twice a day and logs the lowest price available for a specific city, duration and headcount.
- IF the price falls below a certain value, it sends a notification to the user as an email.
- Future plans is to make a flask api for this application

## Installation:

- Clone this repository

```
git clone https://github.com/sunny-k-singh/SeleniumProject.git
```

- Then go into BookingsCOMbot folder > Bookings > booking.py and edit the driver path to the path of your downloaded chromedriver. This will edit the ` $PATH` to include the path to the webdriver.
- Then simply execute:

```
python run.py destination_name start_date end_date headcount filter
```

- start and end dates must be in `YYYY-MM-DD` format.
- The default behaviour is to search for the lowest prices. filter argument must be either **price**, **class** or **price_and_class**.
