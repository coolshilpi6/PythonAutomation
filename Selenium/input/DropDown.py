"""
This tests shows the drop and down automation using selenium
"""
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("C:\driver\chromedriver_win32\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

drp = Select(driver.find_element_by_id("RESULT_RadioButton-9"))
drp.select_by_visible_text("Morning")

drp.select_by_index(2)

drp.select_by_value("Radio-2")

# Count no of options
print(len(drp.options))
options = [x.text for x in drp.options]
# Capture all the options and print
print(*options, sep=", ")

driver.close()
