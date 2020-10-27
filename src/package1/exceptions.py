
i=5
j=0

#print(i/j)

try:
    k=i/j
    print(k)
except ZeroDivisionError as except1:
    if except1:
        return "hello inproper input"
    else:
        print("nothing happend")
else:
    print("waiting")
    
try:
    k=i/j
    print(k)
except ZeroDivisionError as except1:
    if except1:
        def some_logic():
            pass
    else:
        print("nothing happend")
else:
    print("waiting")