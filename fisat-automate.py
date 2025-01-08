from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
actualTitle = driver.title
try:
    driver.get("https://fisat.ac.in/")
    nametextbox=driver.find_element(By.ID,"menu-item-dropdown-4054")
    nametextbox.click()
    academis=driver.find_element(By.ID,"menu-item-dropdown-4059")
    academis.click()
    department=driver.find_element(By.ID,"menu-item-dropdown-4144")
    department.click()
    time.sleep(5)
    if actualTitle=="Computer Applications | FISAT | Federal Institute of Science And Technology":
        print("PASSED")
    else:
        print("FAILED")
finally:
    driver.quit()