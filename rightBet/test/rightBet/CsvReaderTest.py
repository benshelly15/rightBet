'''
Created on 10 Feb 2016

@author: BenShelly
'''
import unittest
from rightBet.CsvReader import CsvReader


class Test(unittest.TestCase):


    def setUp(self):
        global csvReader
        csvReader = CsvReader()


    def tearDown(self):
        pass


    def testReadFile(self):
        global csvReader
        horseOddsArray = csvReader.readCsv()
        self.assertEquals(len(horseOddsArray), 30, "test failed")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
