# D:\WORKSPACE\PYTHON\PYTHON_BOOTCAMP\src\IO

with open('D:/WORKSPACE/PYTHON/PYTHON_BOOTCAMP/src/IO/temp.txt') as file_object:
    contents = file_object.read()
    #print(contents)
    
filename = 'D:/WORKSPACE/PYTHON/PYTHON_BOOTCAMP/src/IO/temp.txt'
with open(filename) as file_object:
    for line in file_object:
        pass
        #print(line.rstrip())
        

# filename = 'D:/WORKSPACE/PYTHON/PYTHON_BOOTCAMP/src/IO/temp.txt'
# 
# with open(filename) as file_object:
#     lines = file_object.readlines()
#     #print(lines)
#     for line in lines:
#         pass
#         #print(line.rstrip())  
#         
# 
# filename = 'D:/WORKSPACE/PYTHON/PYTHON_BOOTCAMP/src/IO/temp.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
#      
# pi_string = ''
# for line in lines:
#     pi_string += line.rstrip()
#     print(pi_string)
#     print(len(pi_string)) 
    
# filename = 'D:/WORKSPACE/PYTHON/PYTHON_BOOTCAMP/src/IO/temp.txt'
# 
# with open(filename) as file_object:
#     lines = file_object.readlines()
#     
# pi_string = ''
# for line in lines:
#     pi_string += line.rstrip()
#     
# birthday = input("Enter your birthday, in the form mmddyy: ")
# if birthday in pi_string:
#     print("Your birthday appears in the first million digits of pi!")
# else:
#     print("Your birthday does not appear in the first million digits of pi.")  
    
    
filename = 'D:/WORKSPACE/PYTHON/PYTHON_BOOTCAMP/src/IO/programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")
    
filename = 'D:/WORKSPACE/PYTHON/PYTHON_BOOTCAMP/src/IO/programming1.txt'
with open(filename, 'a') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")

