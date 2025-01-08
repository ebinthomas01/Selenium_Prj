
from selenium  import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()

"""strip() is used to avoid white spaces"""
try:
    driver.get("file:///C:/Users/ebint/Desktop/Selenium_Prgms/index.html")
    time.sleep(2)
    check_element = driver.find_element(By.TAG_NAME,"h1")
    if check_element.text.strip()=="FISAT":
        nameTextBox = driver.find_element(By.NAME,"fname")
        nameTextBox.send_keys("Ebin")
        time.sleep(5)
        print("PASSED")
    else:
        print("FAILED")

finally:
    driver.quit()