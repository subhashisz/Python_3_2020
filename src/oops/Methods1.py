

class Caller:
    x = 5

    if __name__ == '__main__':
        print("in main method ..........")
     
    def __init__(self):
        print(("inside constructor .............. "))
     
    def meth(self):
        print("inside meth() method ...........")
     
    @classmethod
    def configure(self):
        print("inside configure method ...........")

     
Obj=Caller()
print(Obj.configure())
