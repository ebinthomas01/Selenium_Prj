# Selenium_Prj
This contains selenium projects with is tested

////////// Common importing things /////////

from selenium  import webdriver
from selenium.webdriver.common.by import By
import time

///////// Normally Uses chrome /////////

driver=webdriver.Chrome()


try:
    driver.get("file:///C:/Users/ebint/Desktop/Selenium_Prgms/index.html")
    time.sleep(5)

finally:
    driver.quit()



///////// To Run the command /////////

python web-automate.py


//////// To run pytest ///////////

python -m pytest 


/////// To make report using pytest /////////

python -m pytest --html=report.html
