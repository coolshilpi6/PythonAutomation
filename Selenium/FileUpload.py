import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\driver\chromedriver_win32\chromedriver.exe")

driver.get("http://testautomationpractice.blogspot.com/")

driver.maximize_window()

driver.switch_to.frame(0)

driver.find_element(By.XPATH, "//*[@id='RESULT_FileUpload-11']").send_keys("C://Users/Shilpi Das/PycharmProjects/PythonAutomation/Selenium/big-logo.png")

time.sleep(5)
driver.close()
