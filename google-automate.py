from selenium import  webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()

try:
    driver.get("https://www.google.com/")
    time.sleep(5)
    text_Box=driver.find_element(By.ID,"APjFqb")
    text_Box.send_keys("FISAT")
    text_Box.send_keys(Keys.ENTER)
    
    time.sleep(5)

finally:
    driver.quit()