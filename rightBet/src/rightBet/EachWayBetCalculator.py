'''
Created on 16 Jan 2016

@author: BenShelly
'''
from rightBet.WinBetCalculator import WinBetCalculator

class EachWayBetCalculator():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def calculate(self, stake, odds, place):
        winAmount = 0.00
        if place > 0 and place < 5:
            halfStake = stake / 2
            if place == 1:
                wbcalc = WinBetCalculator()
                winAmount = wbcalc.calculate(halfStake, odds, place)
            else:
                winAmount = halfStake
            winAmount = (winAmount) + ((halfStake) * (odds / 4))
            
        return round(winAmount, 2)
