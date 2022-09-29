# GIANT EAGLE PAGE SCRAPE
# Dynamic page scrap that use react or google (non json files)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# This installs the Chrome driver for Selenium (browser automation API)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# navigates to a webpage
driver.get('https://shop.gianteagle.com/crafton/weekly-ad/')

# requested browser information (in this case the title)
title = driver.title

# either price box is needed to pull items
# price_box = driver.find_elements(by=By.CLASS_NAME, value="tabular")
price_box = driver.find_elements(by=By.CLASS_NAME, value="SharedProductPricingDetails")
item_box = driver.find_elements(by=By.TAG_NAME, value="a")

for x in item_box:
    print(x.text)


driver.quit()





