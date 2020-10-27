try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")
except FileNotFoundError:
    pass

import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)