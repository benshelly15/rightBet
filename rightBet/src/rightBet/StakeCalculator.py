'''
Created on 10 Feb 2016

@author: BenShelly
'''

class StakeCalculator(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        __stake = 0
        
        
    def setStake(self, stake):
        total = 0
        stake = int(input("Input Stake\n")) 
        stake = round(stake, 2)
    
        total = (total) + (stake)
        
        return total
    
    def getStake(self):
        return self.setStake()