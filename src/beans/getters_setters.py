'''
Created on Oct 26, 2020

@author: SUBHASHIS
'''
class P:

#     def __init__(self,x):
#         self.__x = x
    __x=int
    
    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x


class AnotherClass:
    
    obj=P()
    obj.set_x(42)
    print(obj.get_x())
    
# class OurClass:
# 
#     def __init__(self, a):
#         self.OurAtt = a
# 
# 
# x = OurClass(10)
# print(x.OurAtt)


class OurClass:

    def __init__(self, a):
        self.OurAtt = a

    @property
    def OurAtt(self):
        return self.__OurAtt

    @OurAtt.setter
    def OurAtt(self, val):
        if val < 0:
            self.__OurAtt = 0
        elif val > 1000:
            self.__OurAtt = 1000
        else:
            self.__OurAtt = val


x = OurClass(10)
print(x.OurAtt)

