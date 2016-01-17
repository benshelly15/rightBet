'''
Created on 17 Jan 2016

@author: BenShelly
'''
import unittest
from rightBet.HorseOdds import HorseOdds


class Test(unittest.TestCase):
    horseOdds = None
    

    def setUp(self):
        self.horseOdds = HorseOdds () 


    def tearDown(self):
        pass


    def testSetHorseName(self):
        self.horseOdds.setHorseName("dave")
        self.assertEquals(self.horseOdds.getHorseName(), "dave", "testfailed") 
        
    def testSetHorseOddsDecimal(self):
        self.horseOdds.setHorseOddsString("11/2")
        self.assertEquals(self.horseOdds.getHorseOddsDecimal(),5.50, "testfailed")     
     
    def testSetHorseOddsString(self):
        self.horseOdds.setHorseOddsString("11/2")
        self.assertEquals(self.horseOdds.getHorseOddsString(),"11/2", "testfailed")    
        
    def testSetHorseOddsNumber(self):
        self.horseOdds.setHorseNumber(10)
        self.assertEquals(self.horseOdds.getHorseNumber(),10, "testfailed") 


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()