

# Method example
def greet_user():
    """Display a simple greeting."""
    print("Hello!")


# Method example
'''    METHOD WITH NO ARGUMENT          '''


# Print the value of a message   
def display_message(message):
    print("Displaying message :" + message)


def get_message():
    message = input("enter a valid message :") 
    display_message(message)

# get_message()


''' METHOD WITH DEFAULT ARGUMENT'''


def hello(name="everybody"):
    """ Greets a person """
    print("Hello " + name + "!")

# hello("Peter")
# hello()


def spammer(bag=[]):
    ''' THIS IS  A DOC STRING '''
    bag.append("spam")
    return bag

# print(spammer())
# print(spammer())
# print("spammer.__defaults__", spammer.__defaults__)
# print("spammer.__docstring__", spammer.__doc__)


''' METHOD WITH POSITIONAL ARGUMENT '''
'''In case of positional argument order matters means the order in which the argument is passed in that order it was manupulated '''


def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

    
''' METHOD WITH KEY_WORD AS ARGUMENT'''
'''In case of keyword argument it depends on the argument passed but does not depend on the order in which it was passed '''


def sumsub(a, b, c=0, d=0):
    return a - b + c - d

# print(sumsub(12, 4))
# print(sumsub(42, 15, d=10))
# print(sumsub(42, 15,1,10))
# print(sumsub(42, 15,c=5))
# print(sumsub(42, 15,6))


def describe_pet1(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

    
describe_pet(animal_type='hamster', pet_name='harry')  # while passing the value parameter names are specified 
    
''' METHOD WITH VARIABLE AS ARGUMENT'''

'''  '''


def f1(): 
    print(s1)

    
s1 = "GLOBAL VARIABLE ........"  # GLOBAL VARIABLE
f1()


def f2():
    s2 = "METHOD LOCAL VARIABLE .......... "
    print(s2)


f2()


def f3():
    pass
    # print(s2) CAN NOT ACCESS s2 BECAUSE IT IS A METHOD LOCAL VARIABLE


def f4():
    global s 
    # print(s)
    s = "METHOD LOCAL VARIABLE"
   # print(s)


s = "GLOBAL VARIABLE" 
f4()
# print(s)


def arithmetic_mean(first, *values):
    """ This function calculates the arithmetic mean of a non-empty
        arbitrary number of numerical values """

    return (first + sum(values)) / (1 + len(values))

# print(arithmetic_mean(45,32,89,78))
# print(arithmetic_mean(8989.8,78787.78,3453,78778.73))
# print(arithmetic_mean(45,32))
# print(arithmetic_mean(45))


x = [3, 5, 9]
print(arithmetic_mean(12, *x))

my_list = [('a', 232, "e", 1),
           ('b', 343, "f", 2),
           ('c', 543, "g", 3),
           ('d', 23, "h", 4)] 
print(list(zip(*my_list)))


def f(**kwargs):
    print(kwargs)


f()


def f10(a, b, x, y):
    print(a, b, x, y)


d = {'a':'append', 'b':'block', 'x':'extract', 'y':'yes'}
f10(**d)

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

        
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')



