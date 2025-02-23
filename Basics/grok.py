

# a = int(input('Your number is: '))
# b = int(input('Your number is: '))
# c = (input('Your operation is: '))

# if a and b != 0:
#     if c == '/':
#         print(a / b)
#     elif c == '*':
#         print(a * b)
#     elif c == '+':
#         print(a + b)
#     elif c == '-':
#         print(a - b)
#     else:
#         print('Error symbol')
# else:
#     print('Please change num 0')


# a = input('Your numbers: ')

# list_items = a.split(',')

# for i in list_items:


# print(list_items)

# shop = {}

# promt = 'Your fruit: '
# promt2 = 'Your quantity: '

# active = True

# while active:
#     fruit = input(promt)
#     if fruit == 'quit':
#         active = False
#         print(shop)
#         print('Sum all quantity:', sum(shop.values()))
#         break
#     quantity = int(input(promt2))
#     shop[fruit] = quantity
#     print(shop)


import random

length = int(input('your length '))

alf = [chr(i) for i in range(97, 123)]

password = [] 
f = random.randint(6, 15)
print(f)