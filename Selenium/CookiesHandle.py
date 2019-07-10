import time

from selenium import webdriver

driver = webdriver.Chrome("C:\driver\chromedriver_win32\chromedriver.exe")

driver.get("https://www.amazon.in/")

# Capture all the cookies created by browser
cookies = driver.get_cookies()
print("No Of cookies", len(cookies))

print("Cookies", cookies)

# Add new cookie to browser
cookie = {'name': "MyCookie", "value": "1234567"}
driver.add_cookie(cookie)
print("Length of Cookies After Addition", len(driver.get_cookies()))

# Deleting the cookie
driver.delete_cookie("MyCookie")
time.sleep(3)
print("Length of Cookies After Deletion", len(driver.get_cookies()))

# Deleting all the cookies
driver.delete_all_cookies()
time.sleep(3)
print("Length of Cookies", len(driver.get_cookies()))
driver.close()
