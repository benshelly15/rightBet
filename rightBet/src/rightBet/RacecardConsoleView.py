'''
Created on 10 Feb 2016

@author: BenShelly
'''

class RacecardConsoleView(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def printRacecard(self, horseOddsArray):
        for horseOdds in horseOddsArray:
            print(horseOdds.toString())