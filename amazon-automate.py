from selenium import webdriver
from selenium.webdriver.common.by  import By

""" To make enter """
from selenium.webdriver.common.keys import Keys     
import time
driver=webdriver.Chrome()

try:
    driver.get("https://www.amazon.in")
    time.sleep(2)
    pTextBox = driver.find_element(By.ID,"twotabsearchtextbox")
    pTextBox.send_keys("Samsung s24 ultra")

    """To Make Enter the search button"""
    pTextBox.send_keys(Keys.ENTER)
    time.sleep(5)
    print("PASSED")
finally:
    driver.quit()
