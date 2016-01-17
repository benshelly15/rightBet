'''
Created on 17 Jan 2016

@author: BenShelly
'''

class HorseOdds():
    '''
    classdocs
    '''
    horseOddsString = ("")
    horseOddsDecimal = 0.0
    horseNumber = 0
    horseName = ("")

    def __init__(self):
        '''
        Constructor
        '''
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
        
    def setHorseName (self,hn):
        self.horseName = hn 
    