'''
Created on 10 Feb 2016

@author: BenShelly
'''
import unittest
from rightBet.StakeCalculator import StakeCalculator


class Test(unittest.TestCase):


    def setUp(self):
        self.stakeCalculator = StakeCalculator ()


    def tearDown(self):
        pass


    def stakeTotal(self):
        self.stakeCalcultor.stake(5.00)
        self.assertEquals(self.stakeCalulator.stake(5.00), 5.00, "calculated wrong")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
