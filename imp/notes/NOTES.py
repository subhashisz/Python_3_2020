
'''
Especialy for those migrating from Python 2.x to Python 3.x: zip() used to return a list, now it's returning an iterator.
You have to keep in mind that iterators exhaust themselves, if they are used. You can see this in the following interactive 
session:
'''

'''
DICTIONARY CONVERTING FROM ZIP TO LIST
'''

l1 = ["a","b","c"]
l2 = [1,2,3]
c = zip(l1,l2)
z1 = list(c)
z2 = list(c)
print(z1) # OUTPUT: [('a', 1), ('b', 2), ('c', 3)]
print(z2) # OUTPUT: [] this is because list of zip will return an iterator(more info required)


'''  

'''

'''
In case of List copy method will do shalow_copy so the relevant objects are not copied. When a List contains another List object 
then it is safer to go for deepcopy.
'''
#SHALOWCOPY
person1 = ["Swen", ["Seestrasse", "Konstanz"]]
person2 = person1.copy()
person2[0] = "Sarah" # value will be changed in both person1 and person2 because copy method will provide a shalowcopy
print(person1)
print(person2)



#DEEPCOPY
from copy import deepcopy
person1 = ["Swen", ["Seestrasse", "Konstanz"]]

person2 = deepcopy(person1)
person2[0] = "Sarah" # #value will be changed in  person1  because we are doing deepcopy

'''TERNARY OPERATOR EXAMPLE'''
inside_city_limits = False
maximum_speed = 50 if inside_city_limits else 100
print(maximum_speed)


'''
DEFAULT VALUE IN FUNCTIONS
'''
'''
Never use mutable objects as default argument in any function/method, because multiple invocation will give unexpected output
'''

def spammer(bag=[]):
    bag.append("spam")
    return bag

print(spammer()) # OUTPUT: ['spam']
print(spammer()) # OUTPUT: []

'''
GLOBAL
'''

'''
global statement inside the nested function g does not affect the variable 'city' of the function f, i.e. it keeps its value 'Hamburg'. 
'''

def f():
    city = "Hamburg"
    def g():
        global city
        city = "Geneva"
    print("Before calling g: " + city)
    print("Calling g now:")
    g()
    print("After calling g: " + city)


f()


'''
NONLOCAL
'''

'''
nonlocal bindings can only be used inside of nested functions. A nonlocal variable has to be defined in the enclosing function scope. 
If the variable is not defined in the enclosing function scope, the variable cannot be defined in the nested scope. This is another difference
to the "global" semantics.

'''

def f1():
    city = "Munich"
    def g1():
        nonlocal city
        city = "Zurich"
    print("Before calling g: " + city)
    print("Calling g now:")
    g1()
    print("After calling g: " + city)
    
city = "Stuttgart"
f1()
print("'city' in main: " + city)

'''
A program to count the instances of the class. Doubt is what is type(self).count_instances?
'''

class InstanceCounter: 
    count_instances = 0
    
    def __init__(self): 
        type(self).count_instances += 1 # What is type(). If we remove type() then we got output 0 in every case. My observation is 
                                        # it is not static.

    def __del__(self):
        type(self).count_instances -= 1


if __name__ == "__main__":
    x = InstanceCounter()
    print("Number of instances: : " + str(InstanceCounter.count_instances))
    y = InstanceCounter()
    print("Number of instances: : " + str(InstanceCounter.count_instances))
    del x
    print("Number of instances: : " + str(InstanceCounter.count_instances))
    del y
    print("Number of instances: : " + str(InstanceCounter.count_instances))