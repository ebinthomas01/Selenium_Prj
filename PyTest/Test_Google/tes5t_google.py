from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver1=webdriver.Chrome()

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
def google():
    try:
        driver.get("https://www.google.com/")
        driver.save_screenshot("image.png")
        return driver.title
        time.sleep(2)
    finally:
        driver.quit()
def google_search():
    try:
        driver1.get("https://www.google.com/")
        # searchBox=driver.find_element(By.XPATH,"//*[@id='APjFqb']")   #copy xpath
        searchBox=driver1.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea")  #copy full xpath
        searchBox.send_keys("iphone")
        searchBox.send_keys(Keys.ENTER)
        time.sleep(2)

        WebDriverWait(driver1,10).until(expected_conditions.presence_of_element_located((By.ID,"search")))
        searchResult=driver1.find_elements(By.XPATH,"//h3[contains(@class,'LC20lb')]")
        print(searchResult)
        print(len(searchResult))
        return len(searchResult)
       
    finally:
        driver1.quit()
def test_google():
    assert google()=="Google"

def test_google_search():
    assert google_search()>0