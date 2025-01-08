from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

def fisat():
    try:
        driver.get("https://www.google.com/")
        
       
        searchBox = driver.find_element(By.XPATH, "//textarea[@name='q']")
        searchBox.send_keys("fisat")
        searchBox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "search")))
        searchResult = driver.find_elements(By.XPATH, "//div[@id='search']//h3")
        print([result.text for result in searchResult])  
        print(len(searchResult))
        return len(searchResult)
    finally:
        driver.quit()

def test_fisat():
    assert fisat() > 0, "No search results found!"
