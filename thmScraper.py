# Imports
# Python3 dependencies found in requirements.txt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import csv

# Function to scrape data
def scrape(data, index):

    # Configure Selenium web driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument('--headless')
    
    # Prepares For Loop to run once for single entry or fully iterate for all
    startPoint = index
    if(index == -1):
        startPoint = 0
        index = len(data[0]) - 1

    # Instantiates return value and web driver
    retValue = ''
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    # Main Loop for Scraping
    for x in range(startPoint, index+1):

        # Connect to site and scrape rooms completed
        # URL format: "https://www.tryhackme.com/p/[USER NAME]"
        url = 'https://www.tryhackme.com/p/' + data[1][x]
        browser.get(url)
        
        # Waits for page to load and responsive JS to run
        timeout = 10
        try:
            # Interrups wait when the text changes from "Loading..." to the list of rooms completed
            # If the program ever breaks it's probably this that needs to get changed (x-path and/or methodology)
            WebDriverWait(browser, timeout).until_not(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="completed-rooms"]'), 'Loading...'))

            # Grabs list of completed rooms by x-path
            rooms = browser.find_element_by_xpath('//*[@id="completed-rooms"]').text
            count = rooms.split('\n')
            count = sorted(count[::2])
            
            # Adds data to return value string
            retValue += ('\nName: ' + data[0][x] + '\n')
            retValue += ('User: ' + data[1][x] + '\n')
            retValue += ('Completed Rooms:\n')
            for s in count:
                retValue += '\t-'
                retValue += s
                retValue += '\n'
        
        # Doesn't quit browser so if one user in the middle fails the others still go
        except TimeoutException:
            retValue += ("Site failed to load for" + data[0][x] + "(is the username correct?)\n")

    # Returns string built with values
    return retValue


# Main method
if __name__ == '__main__':
    
    # Gets username data from CSV and formats it
    with open('fisData.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    data = list(zip(*data))

    # Gets choice and calls scraper function accordingly
    print('Enter last name to search or enter for all entries')
    userChoice = input()
    if(userChoice == ''):
        print(scrape(data, -1))
    else:
        try:
            index = data[0].index(userChoice)
            print(scrape(data, index))
        except ValueError:
            print("Name not found")