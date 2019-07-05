import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\driver\chromedriver_win32\chromedriver.exe")
#http://newtours.demoaut.com/
driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title)
print("_____________________________________________________")
#print(driver.page_source)
print("_____________________________________________________")
print(driver.current_url)
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

time.sleep(5)
#driver.close() close current browser

driver.quit() #all browsers