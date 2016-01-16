'''
Created on 16 Jan 2016

@author: BenShelly
'''
import unittest
from rightBet.winBetCalculator import WinBetCalculator


class Test(unittest.TestCase):


    def setUp(self):
        global calc
        calc = WinBetCalculator()


    def tearDown(self):
        pass


    def testFiveToOne(self):
        global calc
        self.assertEquals(calc.calculateWinBet(1.00, 5.00),6.00, "odds are wrong")
    
    def testRoundingToTwoDP(self):
        global calc
        self.assertEquals(calc.calculateWinBet(1.25, 5.50),8.12, "odds are wrong")
    
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()