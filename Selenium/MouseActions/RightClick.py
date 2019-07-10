"""
This test automates right click
"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\driver\chromedriver_win32\chromedriver.exe")

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

driver.maximize_window()

btn=driver.find_element(By.XPATH,"/html/body/div/section/div/div/div/p/span")

actions=ActionChains(driver)

actions.context_click(btn).perform()

time.sleep(5)
driver.close()