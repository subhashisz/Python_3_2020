
# Python3 code to demonstrate 
# Assigning range of elements to List 
# using extend() 
  
# initializing list 
test_list = [3, 5, 6, 8] 
  
# printing original list 
print("The original list : " + str(test_list)) 
  
# using extend() 
# Assigning range of elements to List 
test_list.extend(range(6)) 
  
# print result 
print("The list after adding range elements : " + str(test_list)) 

# Python3 code to demonstrate 
# Assigning range of elements to List 
# using * operator 
  
# initializing list 
test_list = [3, 5, 6, 8] 
  
# printing original list 
print("The original list : " + str(test_list)) 
  
# using * operator 
# Assigning range of elements to List 
res = [3, 5, *range(6), 6, 8] 
  
# print result 
print("The list after adding range elements : " + str(res)) 

print(*range(5))

