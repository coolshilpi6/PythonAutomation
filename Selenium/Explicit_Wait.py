import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome("C:\driver\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.expedia.com/")

# driver.find_element_by_id("tab-flight-tab-hp").click()
driver.find_element(By.ID, "tab-flight-tab-hp").click()
time.sleep(2)
driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")
time.sleep(2)

driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")
time.sleep(2)

depart_date = driver.find_element(By.ID, "flight-departing-hp-flight")
return_date = driver.find_element(By.ID, "flight-returning-hp-flight")

depart_date.clear()
depart_date.send_keys("07/06/2019")
driver.execute_script("window.scrollTo(0, 50)")
driver.find_element_by_xpath("//*[@id='flight-departing-wrapper-hp-flight']/div/div[2]/div[1]/button").click()

# return_date.clear()
# time.sleep(5)
# return_date.send_keys("08/05/2019")

# time.sleep(2)
wait = WebDriverWait(driver, 10)
submit = wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button")))
if submit.is_displayed():
    submit.click()

# Next Page Explicit wait

element = wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='stopFilter_stops-0']")))
element.click()
time.sleep(3)
driver.quit()
