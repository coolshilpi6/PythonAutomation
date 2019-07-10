"""
This code is responsible for performing data driven test
The test data is present in TestData.clsx


"""
from selenium import webdriver
from selenium.webdriver.common.by import By

from Selenium.dataDriven import XLUtils

driver = webdriver.Chrome("C:\driver\chromedriver_win32\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")
driver.maximize_window()
path = "C://Users/ShilpiDas/PycharmProjects/PythonAutomation/Selenium/TestData.xlsx"

rows = XLUtils.getRowCount(path, "Sheet1")
for r in range(2, rows + 1):
    userName = XLUtils.readData(path, "Sheet1", r, 1)
    password = XLUtils.readData(path, "Sheet1", r, 2)
    driver.find_element(By.NAME, "userName").send_keys(userName)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "login").click()

    # Writing the test result in a column if test is passed or failed
    if driver.title == "Find a Flight: Mercury Tours:":
        print("Test Passed")
        XLUtils.writeData(path, "Sheet1", r, 3, "Test Passed")
    else:
        print("Test failed")
        XLUtils.writeData(path, "Sheet1", r, 3, "Test Failed")

    driver.find_element(By.LINK_TEXT, "Home").click()

driver.close()
