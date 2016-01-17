'''
Created on 16 Jan 2016

@author: BenShelly
'''
import unittest
from rightBet.EachWayBetCalculator import EachWayBetCalculator


class Test(unittest.TestCase):


    def setUp(self):
        global calc
        calc = EachWayBetCalculator()


    def tearDown(self):
        pass


    def testName(self):
        global calc
        self.assertEquals(calc.calculate(2.00, 4.00, 1), 6.00, "odds are wrong")

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
