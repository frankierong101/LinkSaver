import os
import re
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service

#Set path to edge webdriver
current_dir = os.path.dirname(os.path.abspath(__file__))
EDGE_DRIVER_PATH = os.path.join(current_dir, "msedgedriver.exe")

#Stores last visited URL
file_path = os.path.join(current_dir, "tracked_url.txt")

#Loads last visited URL from txt file if available
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        last_url = file.read().strip()
        if not last_url:  #If file is empty
            last_url = "https://www.apple.com/ie/"
else:
    last_url = "https://www.apple.com/ie/"

#Initialises WebDriver for Edge
service = Service(EDGE_DRIVER_PATH)
driver = webdriver.Edge(service=service)
driver.get(last_url)

try:
    while True:
        current_url = driver.current_url  
        if current_url != last_url:
            last_url = current_url  
            
            #Saves the new URL for next restart
            with open(file_path, "w") as file:
                file.write(current_url)
            #Prints updated URL and seed
            print(f"Updated URL:\n{current_url}")

        time.sleep(1)  #Checka every second

except KeyboardInterrupt:
    print("Tracking stopped by user.")
    
finally:
    driver.quit()
