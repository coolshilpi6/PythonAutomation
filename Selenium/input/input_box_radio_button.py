"""
This file automates input box and radio button
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("C:\driver\chromedriver_win32\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
time.sleep(5)
# find how many input boxes present in web page
inputBoxes = driver.find_elements(By.CLASS_NAME, 'text_field')
print(len(inputBoxes))

assert len(inputBoxes) == 8

driver.find_element(By.ID, "RESULT_TextField-1").send_keys("pavan")
driver.find_element(By.ID, "RESULT_TextField-2").send_keys("kumar")

driver.find_element_by_id("RESULT_TextField-3").send_keys("65789045312")

# driver.execute_script("window.scrollTo(0, 300)")
# wait = WebDriverWait(driver, 10)
# element = wait.until(ec.element_to_be_clickable((By.ID, "RESULT_RadioButton-7_0")))
# element.click()
# time.sleep(5)
# Radio Button
action = ActionChains(driver)
male_rb = driver.find_element(By.XPATH, "//*[@id='RESULT_RadioButton-7_1']")
action.move_to_element(male_rb).perform()
print(male_rb.is_selected())
male_rb.click()
time.sleep(3)

driver.quit()
