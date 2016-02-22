'''
Created on 10 Feb 2016

@author: BenShelly
'''
from rightBet.HorseOdds import HorseOdds
from rightBet.WinBetCalculator import WinBetCalculator
from rightBet.EachWayBetCalculator import EachWayBetCalculator
import datetime
class BettingSlipConsoleView(object):
    '''
    classdocs
    '''
    
    
    def __init__(self):
        '''
        Constructor
        '''
        self.__winBet = WinBetCalculator ()
        self.__ewBet = EachWayBetCalculator ()
        
    def printToConsole(self, selectedHorses):
        print("============================\n")
        print("== Right Bet Betting Slip ==\n")
        print("============================\n")
        totalCost = 0.00
        potentialWin = 0.00
        for horseOdds in selectedHorses:
            if horseOdds.isWinBet():
                currentWin = self.__winBet.calculate(horseOdds.getStake(), horseOdds.getHorseOddsDecimal(), 1)
                print(self.bettingLine(horseOdds, currentWin))
            totalCost = (totalCost) + float((horseOdds.getStake()))
            potentialWin = (potentialWin) + (currentWin)
        
        print("============================\n")
        print("Total Stake is " + str(totalCost))
        print("Maximum potential win is " + str(potentialWin))
        print("Time of bet " + self.dateTime())
        
            
            
             
    def bettingLine(self, horseOdds, potentialWinnings):
        retStr = horseOdds.toString()
        retStr = (retStr) + (" stake ")
        retStr = (retStr) + (horseOdds.getStake())
        retStr = (retStr) + (" winnings: ")
        retStr = (retStr) + ("{:.2f}".format(potentialWinnings))
        
        return (retStr)
        
                
    def dateTime(self):
        timedate = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        return (timedate)       
