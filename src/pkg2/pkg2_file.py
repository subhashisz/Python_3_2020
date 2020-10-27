

class SuperClass:  # public super class
    
    name = str        # public member
    age = float       # public member
    address = str     # public member
    any_value = None  # public member
    
    _protected_variable = str  # Protected member single underscore
    __private_variable = str  # private member double underscore
    
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    if __name__ == '__main__':
        print("Inside main method ......")
        
    # Instance method
    def a_print_method(self):
        print(" You called this method by object reference ......")
    
    @classmethod
    def class_method_example(any_arg):
        print(" Inside class method ....")

    @classmethod
    def class_method_example2(any_arg):
        print(" Inside class method ....")

    @staticmethod
    def static_method_example(any_arg):
        print(" Inside class method ....")

        
class BaseClass(SuperClass):  # Public base class
    
    def __init__(self):
        super()


class _PrivateClass:  # Private class one underscore 
    pass
