import unittest

from selenium import webdriver


class Test(unittest.TestCase):
    def test_firstTest(self):
        print("This in my 1st test case")

    def test_Google(self):
        self.driver = webdriver.Chrome("C:\driver\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://google.com/")
        print("Title of Page is:",self.driver.title)
        self.driver.close()

    def test_Bing(self):
        self.driver = webdriver.Chrome("C:\driver\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://bing.com")
        print("Title of Page is:",self.driver.title)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
