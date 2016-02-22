'''
Created on 10 Feb 2016

@author: BenShelly
'''

import csv
import os
from rightBet.HorseOdds import HorseOdds

class CsvReader(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
    
            
    
    
    def readCsv(self):  
        #print (os.getcwd())
        horseOddsArray = []
        with open("horse_name_and_odds.csv") as infile:
            reader = csv.reader(infile)
            for row in reader:
                horseOddsRow = HorseOdds ()
                horseOddsRow.setHorseOddsString(row[2])
                horseOddsRow.setHorseName(row[1])
                horseOddsRow.setHorseNumber(row[0])
                #print (horseOddsRow.toString())
                horseOddsArray.append(horseOddsRow)
                
        return (horseOddsArray)
            
