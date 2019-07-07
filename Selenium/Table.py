from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\driver\chromedriver_win32\chromedriver.exe")

driver.get("file:///C:/Users/Shilpi%20Das/PycharmProjects/PythonAutomation/Selenium/table.html")

rows = len(driver.find_elements(By.XPATH, "/html/body/table/tbody/tr"))  # match all rows in table

cols = len(driver.find_elements(By.XPATH, "/html/body/table/tbody/tr[1]/th"))  # match all cols in a particular row

for i in range(2, rows+1):
    for j in range(1, cols+1):
        print(driver.find_element(By.XPATH, "/html/body/table/tbody/tr[" + str(i) + "]" + "/td[" + str(j) + "]").text, end="     ")
    print("\n")


driver.close()
