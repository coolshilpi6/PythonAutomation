"""
This test automates drag and drop
"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\driver\chromedriver_win32\chromedriver.exe")

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

driver.maximize_window()

src = driver.find_element(By.XPATH, "//*[@id='box6']")
dest = driver.find_element(By.XPATH, "//*[@id='box106']")

actions = ActionChains(driver)

actions.drag_and_drop(src, dest).perform()

time.sleep(5)
driver.close()
