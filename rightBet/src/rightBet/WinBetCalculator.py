'''
Created on 16 Jan 2016

@author: BenShelly
'''

class WinBetCalculator(object):
    '''
    classdocs
    '''


    def __init__(self):
        
        
    
        '''
        Constructor
        '''
        
        
    def calculate(self, stake, odds, place):
        winAmount = 0.00
        floatStake = float(stake)
        if place == 1:
            winAmount = ((floatStake) * (odds)) + (floatStake)
        return round(winAmount, 2)
        
