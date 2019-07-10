import unittest
from Selenium.UnitTestDemo.AssertionsTestCase import Test
from Selenium.UnitTestDemo.Skipping_Test import Apptesting

tc1 = unittest.TestLoader().loadTestsFromTestCase(Test)
tc2 = unittest.TestLoader().loadTestsFromTestCase(Apptesting)

# creating test suite
sanityTest = unittest.TestSuite([tc1, tc2])
unittest.TextTestRunner(verbosity=2).run(sanityTest)
