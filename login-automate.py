from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
try:
        driver.get("http://10.0.16.206:5501/test.html")
        time.sleep(1)
        InpBox1=driver.find_element(By.ID,"username")
        InpBox1.send_keys("admin")
        InpBox2=driver.find_element(By.ID,"password")
        InpBox2.send_keys("12345")
        time.sleep(2)
        Button=driver.find_element(By.ID,"login_button")
        Button.click()
        checkelement=driver.title
        if checkelement=="Dashboard":
            print("PASSED")
            """When the input given are true, then we also need to check for false test cases too"""
            driver.back()
            InpBox1=driver.find_element(By.ID,"username")
            InpBox1.send_keys("asd")
            InpBox2=driver.find_element(By.ID,"password")
            InpBox2.send_keys("asd")
            time.sleep(2)
            Button=driver.find_element(By.ID,"login_button")
            Button.click()
            checkelement=driver.title
            
            """If the input are failed, then that test case must be passed"""

            if checkelement=="Login Page":
                print("PASSED")
            else:
                print("FAILED")
            time.sleep(3)
                
        else:
            print("FAILED")

        

finally:
    driver.quit()