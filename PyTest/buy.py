from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import  time

driver=webdriver.Chrome()

try:
    driver.get("https://www.google.com/")
    driver.maximize_window()
    searchBox=driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
    searchBox.send_keys("Samsung s24 Ultra")
    searchBox.send_keys(Keys.ENTER)
    time.sleep(2)

    clicklink=driver.find_element(By.XPATH,"/html/body/div[3]/div/div[13]/div/div[1]/div[2]/div[2]/div/div/div[4]/div/div/div/div[1]/div/div/span/a/h3")
    clicklink.click()
    time.sleep(2)
    driver.save_screenshot("samsungHomePage.png")

finally:
    driver.quit()
