import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\driver\chromedriver_win32\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")
links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))

options=[x.text for x in links]
# Capture all the links and print
print(*options, sep=", ")

#click on link
driver.find_element(By.LINK_TEXT,"REGISTER").click()

time.sleep(5)

driver.close()