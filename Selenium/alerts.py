from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\driver\chromedriver_win32\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com")

alert_button = driver.find_element(By.XPATH, "//*[@id='HTML9']/div[1]/button")
alert_button.click()
time.sleep(5)

driver.switch_to.alert.accept()
assert driver.find_element_by_id("demo").text == "You pressed OK!"

alert_button.click()
time.sleep(3)

driver.switch_to.alert.dismiss()
assert driver.find_element_by_id("demo").text == "You pressed Cancel!"
