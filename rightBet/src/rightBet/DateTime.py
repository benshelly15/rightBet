'''
Created on 10 Feb 2016

@author: BenShelly
'''

class DateTime(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
    
    def dateTime(self):
        import datetime
        timedate = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        return (timedate)