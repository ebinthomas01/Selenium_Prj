from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com/")

    # For full screen we use maximize window
    driver.maximize_window()
    time.sleep(2)
    actualTitle = driver.title
    if actualTitle == "Google":
        print("PASSED")
        searchBox = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea")
        # We need to change " to ' when we copy the XPATH
        searchBox.send_keys("Iphone 16 pro max")
        searchBox.send_keys(Keys.ENTER)
        time.sleep(3)

        # Correctly use WebDriverWait
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search"))
        )
        
        # Locate the search result
        searchResult = driver.find_element(By.XPATH, "//h3[contains(@class,'LC20lb')]")
        print(len(searchResult.text))  # Printing the text length instead of len(searchBox), which is invalid

        for i in range(0,len(searchResult)):
            print(searchResult[i].text)
        
    else:
        print("FAILED")

finally:
    driver.quit()
