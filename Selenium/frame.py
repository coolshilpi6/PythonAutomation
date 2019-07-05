from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\driver\chromedriver_win32\chromedriver.exe")

driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")

driver.switch_to.frame("packageListFrame") # 1st frame

driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()

time.sleep(3)

driver.switch_to.default_content()

driver.switch_to.frame("packageFrame") # 2nd frame

driver.find_element(By.LINK_TEXT, "HasCapabilities").click()

time.sleep(3)

driver.switch_to.default_content()

driver.switch_to.frame("classFrame") # 3rd frame

driver.find_element(By.XPATH, "/html/body/div[1]/ul/li[5]").click()
