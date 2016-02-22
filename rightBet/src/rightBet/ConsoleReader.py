'''
Created on 10 Feb 2016

@author: BenShelly
'''
from rightBet.CsvReader import CsvReader




class ConsoleReader(object):
    '''
    classdocs
    '''


    def __init__(self, hoa):
        '''
        Constructor
        
        '''
        self.setHorseOddsArray(hoa)
        
        
    def readFromConsole(self):
        horseID = input("Input Horse Name or Number or '-' to finish\n")
        selectedHorse = None
        if horseID == "-":
            return ("-")
        if str(horseID).isdigit():
            selectedHorse = self.findHorseByNumber(horseID)
        else:
            selectedHorse = self.findHorseByName(horseID)
        
        if selectedHorse == None:
            print("Horse could not be found")
            return None
        
        print(selectedHorse.toString())
        stake = input("How much do you want to stake?\n")
        selectedHorse.setStake(stake)
        return selectedHorse

    
    def findHorseByNumber(self, horseNumber):
        retHorse = None
        for horseOdds in self.getHorseOddsArray():
            if horseOdds.getHorseNumber() == horseNumber:
                retHorse = horseOdds
                break 
        return retHorse
    
    def findHorseByName(self, horseName):
        retHorse = None
        for horseOdds in self.getHorseOddsArray():
            if horseOdds.getHorseName() == horseName:
                retHorse = horseOdds
            break 
        return retHorse
    
    def setHorseOddsArray (self, hoa):
        self.__horseOddsArray = hoa
        
    def getHorseOddsArray(self):
        return self.__horseOddsArray
        
            