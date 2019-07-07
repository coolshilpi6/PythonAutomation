import time

from selenium import webdriver

driver = webdriver.Chrome("C:\driver\chromedriver_win32\chromedriver.exe")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.maximize_window()

# driver.execute_script("window.scrollBy(0,1000)","") #scroll by pixel

# scroll to element
#flag = driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
#driver.execute_script("arguments[0].scrollIntoView();", flag)

#Moving till end of page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

time.sleep(5)

driver.close()
