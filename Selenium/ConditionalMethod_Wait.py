from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\driver\chromedriver_win32\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")

driver.implicitly_wait(10)  # time in sec

assert "Welcome: Mercury Tours" in driver.title
ele_user = driver.find_element_by_name("userName")
print(ele_user.is_displayed())
print(ele_user.is_enabled())

ele_pwd = driver.find_element_by_name("password")
print(ele_pwd.is_displayed())
print(ele_pwd.is_enabled())

ele_user.send_keys("mercury")
ele_pwd.send_keys("mercury")
# driver.find_element_by_name("login").click()

# type and its value radio button
# driver.find_element_by_css_selector("input[value=roundtrip]").is_selected()
driver.close()
