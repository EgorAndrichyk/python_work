# name = input('Your name is ')
# print(name)

# car = input('What car is need?\n')
# print(f'i search your {car}')

# restourant = int(input("how many? \n"))
# if restourant > 8:
#     print('sorry')
# else:
#     print('okey')

# num = int(input('your number: '))
# if num % 10 == 0:
#     print(f'{num} okey')
# else:
#     print(f'{num} not okey')



# pizza = 'Your ingridients is? '
# active = True
# while active:
#     messege = input(pizza)
#     if messege != 'quit':
#         print(messege)
#     else:
#         active = False

# prompt = "\nHow old are you?"
# prompt += "\nEnter 'quit' when you are finished. "

# while True:
#     age = input(prompt)
#     if age == 'quit':
#         break
#     age = int(age)

#     if age < 3:
#         print("  You get in free!")
#     elif age < 13:
#         print("  Your ticket is $10.")
#     else:
#         print("  Your ticket is $15.")

# sandwich_orders = ['pastomi','meet','pastomi', 
#                    'vegan', 'spice', 'pastomi', 
#                    'cheese']
# finish_sandwich = []

# print(sandwich_orders)


# while 'pastomi' in sandwich_orders:
#     if not sandwich_orders.remove('pastomi'):
#         continue
#     sandwich = sandwich_orders.pop()
#     print(f'I did sandwich with {sandwich}')
#     finish_sandwich.append(sandwich)

# for sandwich in finish_sandwich:
#     print(sandwich)

# print(sandwich_orders)
# print(finish_sandwich)

# print(sandwich_orders)

# while 'pastomi' in sandwich_orders:
#     sandwich_orders.remove('pastomi')

# print(sandwich_orders)

responses = {}
active = True

while active:
    name = input('Your name ')
    respons = input('what you country ')
    responses[name] = respons

    repeat = input('again?')
    if repeat == 'quit' or 'no':
        active = False
    
for name, respons in responses.items():
    print(f'{name} {respons}')