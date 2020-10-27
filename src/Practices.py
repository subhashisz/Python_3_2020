'''
Created on Sep 27, 2020

@author: SUBHASHIS
'''
import thread

def my_meth():
    print("Inside practices my_meth()")


class MyClass:
    
    def __init__(self):
        print("hello")
        
    def getAge(self):
        age = input("please enter a age :")
        return int(age)
    
    def my_meth(self):
        print()

    age = 25


class MyClass1:

    def instance_method(self):
        return 'instance method called', self

    @classmethod
    def class_method(cls):
        return 'class method called', cls

    @classmethod
    def class_method2():
        return 'class method called' 

    @staticmethod
    def static_method():
        return 'static method called'

