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
        __horseOddsString = ("")
        __horseOddsDecimal = 0.0
        __horseNumber = 0
        __horseName = ("")
        __stake = 0.00
        __winBet = True
        
    def getHorseOddsString(self):
        return self.horseOddsString 
    
    def getHorseOddsDecimal(self):
        return self.horseOddsDecimal
    
    def getHorseNumber(self):
        return self.horseNumber
    
    def getHorseName(self):
        return self.horseName
    
    def getStake(self):
        return self.stake
    
    def isWinBet(self):
        return self.winBet
        
    def setHorseOddsString(self, hos):
        self.horseOddsString = hos 
        self.horseOddsDecimal = eval(hos)
        
    def setHorseNumber(self, hn):        
        self.horseNumber = hn
        
    def setHorseName (self, hn):
        self.horseName = hn
    
    def setStake (self, st):
        self.stake = st
    
    def setWinBet(self, wb):
        self.winBet = wb
        
    def toString (self):
        retStr = ("")
        retStr = (retStr) + str(self.horseNumber).rjust(2) + (" ")
        retStr = (retStr) + self.horseName.ljust(40) + (" ")
        retStr = (retStr) + self.horseOddsString.rjust(6)
        
        return (retStr)
