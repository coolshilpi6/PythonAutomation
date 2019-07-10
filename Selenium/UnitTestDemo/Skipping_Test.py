import unittest


class Apptesting(unittest.TestCase):

    @unittest.SkipTest
    def test_search(self):
        print("This in search test case")

    @unittest.skip("This test is not prepared")
    def test_advancedSearch(self):
        print("This in advanced search test case")

    @unittest.skipIf(1 == 1,"Skip with condition")
    def test_prepaidRecharge(self):
        print("This in prepaid Recharge test case")

    def test_postRecharge(self):
        print("This in Post Recharge test case")

    def test_loginByGmail(self):
        print("This in login gmail test case")

    def test_loginByTwitter(self):
        print("This in login twitter test case")

    if __name__ ==  "__main__":
        unittest.main()
