from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\driver\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element(By.XPATH, "//*[@id='Tabbed']/a/button").click()

print(driver.current_window_handle)  # parent

for x in driver.window_handles:
    driver.switch_to.window(x)
    print(driver.title)
    if driver.title == "Frames & windows":  # specific window handle
        driver.close()

driver.quit()
