import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\driver\chromedriver_win32\chromedriver.exe")

driver.get("http://testautomationpractice.blogspot.com/")

driver.maximize_window()


element=driver.find_element(By.XPATH, "//*[@id='HTML10']/div[1]/button")

actions = ActionChains(driver)
actions.double_click(element).perform()
print(driver.find_element(By.ID,"field1").text)
print(driver.find_element(By.ID,"field2").text)
time.sleep(5)
driver.close()


