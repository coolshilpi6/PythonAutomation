import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome("C:\driver\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.google.com/")

    def testName(self):
        title = self.driver.title
        self.assertEqual("Google", title, "Web page title is not same")
        self.assertNotEqual("Google123", title)

    def testNameTrueFalse(self):
        title = self.driver.title
        self.assertTrue("Google" == title, "Web page title is not same")
        self.assertFalse("Google123" == title)

    def testNameNone(self):
        title = self.driver.title
        # self.assertIsNone(None, "Web page title is not same")
        self.assertIsNotNone(title)

    def testAssertIn(self):
        cookie = {'name': "MyCookie", "value": "1234567"}
        self.driver.add_cookie(cookie)
        cookie = self.driver.get_cookies()
        self.assertIn('name', cookie[0])
        self.assertEqual("MyCookie", cookie[0]['name'])

    @classmethod
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
