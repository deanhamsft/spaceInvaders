import math

user_input = input('Write a number ')
try:
    if user_input.isdigit():
        print(math.sqrt(int(user_input)))
    else:
        print('that\'s not a number')
except ValueError:
    print('not a number')