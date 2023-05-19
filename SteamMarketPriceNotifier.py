from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import http.client, urllib
from datetime import datetime

# Paste here the link of the steam market listings for the item you want to look for
url = "https://steamcommunity.com/market/listings/730/Sticker%20%7C%20m0NESY%20(Holo)%20%7C%20Antwerp%202022"
# Paste here your app API TOKEN and USER KEY from your pushover account (https://pushover.net)
api_token = 'YOUR API TOKEN'
user_key = 'YOUR USER KEY'

# The time between each price check (value in seconds)
loop_sec = 300
# The price you want to get notified
limitPrice = 29.99
# If you have more than one chrome profile, keep "plural" as True
plural = True
# If plural is True, please enter your Google user data path
user_data_dir = "C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data"

def getPrice():
    # Creates a new ChromeOptions object and add the user data and profile arguments:
    options = Options()
    if plural:
        profile_name = "Default"
        options.add_argument(f"--user-data-dir={user_data_dir}")
        options.add_argument(f"--profile-directory={profile_name}")
    options.add_argument('--disable-dev-shm-usage')

    # Creates a new web driver instance for Chrome with the specified profile:
    driver = webdriver.Chrome(options=options)

    # Opens the page
    driver.get(url)
    time.sleep(1)

    # Gets the price value from the webpage
    price = ""
    try:
        elements = driver.find_elements(By.CLASS_NAME, "market_commodity_orders_header_promote")
        price = str(elements[1].text).replace("€", "")
        time.sleep(1)
    except Exception as e:
        print("An error occurred while retrieving the price:", str(e))
        price = None

    return price

def sendNotification(message):
    # Sends a notification with a message to your mobile phone using Pushover API
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
                 urllib.parse.urlencode({
                     "token": api_token,
                     "user": user_key,
                     "message": message,
                 }), {"Content-type": "application/x-www-form-urlencoded"})
    conn.getresponse()

if __name__ == "__main__":
    highValue = 0.00

    while True:
        price = getPrice().replace(",", ".").replace("$", "")
        current_time = datetime.now().strftime("%H:%M:%S")
        # Checks if the current price is the highest price since the program started running
        if float(price) > highValue:
            highValue = float(price)
            print("New price peak!")
            sendNotification(f"New highest value peak: {price}$ | Time {current_time}")

        # Checks if the current price is higher than the limit you define
        if float(price) >= limitPrice:
            print(f"PRICE IS MORE THAN {limitPrice}$! : {price}$ | Time: {current_time}\n\n ---------------------------------- \n")
            sendNotification(f"Price is more than {limitPrice}$: {price}$ | Time {current_time}")
        else:
            print(f"Price is good: {price}$ | Time: {current_time}\n\n ---------------------------------- \n")

        time.sleep(loop_sec)
