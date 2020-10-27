'''
Created on Oct 7, 2020

@author: SUBHASHIS
'''

#import pkg2.Calc.Calc as v

from pkg2 import Calc as v

class CallCalc(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
    def calculate(self):
        return v.Calc.add(1, 2)        
      
Obj=CallCalc()
Obj.calculate()  