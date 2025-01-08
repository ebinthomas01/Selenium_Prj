from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options

chrome_options=Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
driver1=webdriver.Chrome(options=chrome_options)

driver = webdriver.Chrome()


def google():
    try:
        driver.get("https://www.google.com/")
        driver.save_screenshot("google.png")
        return driver.title
        time.sleep(2)
    finally:
        driver.quit()

def google_search():
    try:
        driver1.get("https://www.google.com/")
        time.sleep(1)
        driver1.maximize_window()
        time.sleep(2)

        searchBox = driver1.find_element(By.XPATH, "//textarea[@name='q']")
        searchBox.send_keys("about sandbox")
        searchBox.send_keys(Keys.ENTER)
        time.sleep(2)

        firstlink = driver1.find_element(By.XPATH, "//h3[contains(@class,'LC20lb')]")
        firstlink.click()
        time.sleep(2)

        description_element = driver1.find_element(By.TAG_NAME, "p") 
        description = description_element.text
        return description

    finally:
        driver1.quit()

def test_google():
    assert google() == "Google"

def test_google_search():
    description = google_search()
    assert "sandbox" in description.lower()