from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver1=webdriver.Chrome()

import time
def valid():
    try:
        driver.get("http://10.0.16.206:5501/test.html")
        check_user=driver.find_element(By.NAME,"username")
        check_user.send_keys("admin")
        check_pass=driver.find_element(By.NAME,"password").send_keys("12345")
        click_login=driver.find_element(By.ID,"login_button").click()
        actualTitle=driver.title
        return actualTitle       
    finally:
        driver.quit()
def invalid():
    try:
        driver1.get("http://10.0.16.206:5501/test.html")
        check_user=driver1.find_element(By.NAME,"username")
        check_user.send_keys("admins")
        check_pass=driver1.find_element(By.NAME,"password").send_keys("123456")
        click_login=driver1.find_element(By.ID,"login_button").click()
        error=driver1.find_element(By.ID,"error_message")
        return error
    finally:    
        driver1.quit()
def test_valid():
    assert valid()=="Dashboard"
def test_invalid():
    assert invalid()=="Invalid username or password"