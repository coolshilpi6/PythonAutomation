import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\driver\chromedriver_win32\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
print(driver.title)
driver.get("http://demo.automationtesting.in/Windows.html")
time.sleep(3)
print(driver.title)

driver.back()
time.sleep(3)
print(driver.title)

driver.forward()
time.sleep(3)
print(driver.title)

driver.quit()
