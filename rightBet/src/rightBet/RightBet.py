'''
Created on 10 Feb 2016

@author: BenShelly
'''
from rightBet.CsvReader import CsvReader
from rightBet.RacecardConsoleView import RacecardConsoleView

if __name__ == '__main__':
    csvReader = CsvReader ()
    racecardConsoleView = RacecardConsoleView ()
    horseOddsArray = csvReader.readCsv()
    racecardConsoleView.printRacecard(horseOddsArray)
    
    replay = True
    x = 0
    while replay == True:
        
    