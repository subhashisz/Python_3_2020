'''
Created on Oct 24, 2020

@author: SUBHASHIS
'''

class A:
    a = "I am a class attribute created"

x = A()
y = A()
y.a = "Object attribute" # Object attribute changed

print(x.a)
print(y.a)

A.a="class attribute changed" # class attribute changed

print(x.a)
print(x.__dict__)
print(y.__dict__)
print(A.__dict__)