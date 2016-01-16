'''
Created on 16 Jan 2016

@author: BenShelly
'''

class WinBetCalculator():
    '''
    classdocs
    '''


    def __init__(self):
        
        
    
        '''
        Constructor
        '''
        
        
    def calculate(self, stake, odds, place):
        winAmount = 0.00
        if place == 1:
            winAmount = (stake) * (odds) + (stake)
        return round(winAmount,2)
        
