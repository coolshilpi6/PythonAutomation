import unittest


def setUpModule():
    print("Setup Module")


def tearDownModule():
    print("Tear Down Module")


class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("This is setup")

    @classmethod
    def setUpClass(cls):
        print("This is set up class")

    def test_search(self):
        print("This in search test case")

    def test_advancedSearch(self):
        print("This in advanced search test case")

    def test_prepaidRecharge(self):
        print("This in prepaid Recharge test case")

    def test_postRecharge(self):
        print("This in Post Recharge test case")

    @classmethod
    def tearDown(self):
        print("This is tear down")

    @classmethod
    def tearDownClass(cls):
        print("This is tear down class")

    if __name__ == "__main__":
        unittest.main()
