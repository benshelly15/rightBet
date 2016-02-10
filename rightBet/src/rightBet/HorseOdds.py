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
        
    def getHorseOddsString(self):
        return self.horseOddsString 
    
    def getHorseOddsDecimal(self):
        return self.horseOddsDecimal
    
    def getHorseNumber(self):
        return self.horseNumber
    
    def getHorseName(self):
        return self.horseName
        
    def setHorseOddsString(self, hos):
        self.horseOddsString = hos 
        self.horseOddsDecimal = eval(hos)
        
    def setHorseNumber(self, hn):        
        self.horseNumber = hn
        
    def setHorseName (self, hn):
        self.horseName = hn
    
    def toString (self):
        retStr = ("")
        retStr = (retStr) + str(self.horseNumber).rjust(2) + (" ")
        retStr = (retStr) + self.horseName.ljust(40) + (" ")
        retStr = (retStr) + self.horseOddsString.rjust(6)
        
        return (retStr)
