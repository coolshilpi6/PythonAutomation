from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# download in specific folder
chromeOptions = Options()
chromeOptions.add_experimental_option("prefs",{"download.default_directory":"C:\\Users\ShilpiDas\PycharmProjects\Selenium"})

driver = webdriver.Chrome(executable_path="C:\driver\chromedriver_win32\chromedriver.exe",chrome_options=chromeOptions)

driver.get("http://demo.automationtesting.in/FileDownload.html")

driver.maximize_window()

driver.find_element(By.XPATH, "//*[@id='textbox']").send_keys("Hello")
driver.find_element(By.XPATH, "//*[@id='createTxt']").click()
# click on link to download
driver.find_element(By.ID, "link-to-download").click()
