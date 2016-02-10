'''
Created on 10 Feb 2016

@author: BenShelly
'''
from rightBet.CsvReader import CsvReader
from rightBet.RacecardConsoleView import RacecardConsoleView
from rightBet.ConsoleReader import ConsoleReader

if __name__ == '__main__':
    csvReader = CsvReader ()
    racecardConsoleView = RacecardConsoleView ()
    consoleReader = ConsoleReader ()
    horseOddsArray = csvReader.readCsv()
    racecardConsoleView.printRacecard(horseOddsArray)
    
    replay = True
    x = 0
    selectedHorses = []
    while replay == True:
        selectedHorse = consoleReader.readFromConsole()
        if selectedHorse != "-":
            
            if selectedHorse != None:
                selectedHorses.append(selectedHorse)
                if len(selectedHorses) == 8:
                    replay = False
        else:
            replay = False        