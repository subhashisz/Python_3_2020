'''
Created on Oct 25, 2020

@author: SUBHASHIS
'''
class Robot:
    __counter = 0
    
    def __init__(self):
        type(self).__counter += 1
        
    def RobotInstances(self):
        return Robot.__counter
        

if __name__ == "__main__":
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(x.RobotInstances())
    print(id(x))
    print(id(y))


