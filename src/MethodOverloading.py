from multipledispatch import dispatch 


# passing one parameter 
@dispatch(int, int) 
def product(first, second): 
    result = first * second 
    return result 

# # passing three values
# @dispatch(int,int,int)
# def product(first,second,third):
#     return first+second+third
#   
# # data type of any value as per requirement 
# @dispatch(float, float, float) 
# def product(first, second, third): 
#     result = first * second * third 
#     return result 
 
 
# calling product method with 2 arguments 
product(2, 3, 2)  # this will give output of 12 
product(2.2, 3.4, 2.3)  # this will give output of 17.985999999999997 
