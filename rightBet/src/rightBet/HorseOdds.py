'''
Created on 17 Jan 2016

@author: BenShelly
'''

class HorseOdds(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.__horseOddsString = ("")
        self.__horseOddsDecimal = 0.0
        self.__horseNumber = 0
        self.__horseName = ("")
        self.__stake = 0.00
        self.__winBet = True
        
    def getHorseOddsString(self):
        return self.__horseOddsString 
    
    def getHorseOddsDecimal(self):
        return self.__horseOddsDecimal
    
    def getHorseNumber(self):
        return self.__horseNumber
    
    def getHorseName(self):
        return self.__horseName
    
    def getStake(self):
        return self.__stake
    
    def isWinBet(self):
        return self.__winBet
        
    def setHorseOddsString(self, hos):
        self.__horseOddsString = hos 
        self.__horseOddsDecimal = eval(hos)
        
    def setHorseNumber(self, hn):        
        self.__horseNumber = hn
        
    def setHorseName (self, hn):
        self.__horseName = hn
    
    def setStake (self, st):
        self.__stake = st
    
    def setWinBet(self, wb):
        self.__winBet = wb
        
    def toString (self):
        retStr = ("")
        retStr = (retStr) + str(self.__horseNumber).rjust(2) + (" ")
        retStr = (retStr) + self.__horseName.ljust(40) + (" ")
        retStr = (retStr) + self.__horseOddsString.rjust(6)
        
        return (retStr)
