'''
Created on Oct 13, 2020

@author: SUBHASHIS
'''

def module_function():
    print("module function")

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +"-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " , topping)
        

class MyClass1(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
    if __name__ == '__main__':
        pass