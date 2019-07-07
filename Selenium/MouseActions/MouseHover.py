import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\driver\chromedriver_win32\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")

# Login

driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()

admin = driver.find_element(By.XPATH, "//*[@id='menu_admin_viewAdminModule']/b")
mgnt = driver.find_element(By.XPATH, "//*[@id='menu_admin_UserManagement']")
user = driver.find_element(By.XPATH, "//*[@id='menu_admin_viewSystemUsers']")

actions = ActionChains(driver)
actions.move_to_element(admin).move_to_element(mgnt).move_to_element(user).click().perform()
time.sleep(5)
driver.close()
