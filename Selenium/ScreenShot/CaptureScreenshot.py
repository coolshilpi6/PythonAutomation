from selenium import webdriver

driver = webdriver.Chrome("C:\driver\chromedriver_win32\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")

driver.save_screenshot("C://Users/ShilpiDas/PycharmProjects/PythonAutomation/Selenium/ScreenShot/homepage.png")

driver.get_screenshot_as_file("C://Users/ShilpiDas/PycharmProjects/PythonAutomation/Selenium/ScreenShot/homepage2.png")
driver.close()