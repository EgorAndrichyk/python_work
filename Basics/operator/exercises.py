# alian_color = 'red'

# if alian_color == 'red':
#     print('You win 5 points')
# if alian_color == 'green':
#     print('You win 5 points')

# if alian_color == 'red':
#     print('You win 5 points')
# else:
#     print('You win 10 points')

# if alian_color == 'red':
#     points = 15
# elif alian_color == 'green':
#     points = 10
# elif alian_color == 'yellow':
#     points = 5
# else:
#     print('you lose')

# print(f'You win {points} points')

# age = 65

# if age < 2:
#     human = 'Младенец'
# elif age >=2 and age < 4:
#     human = 'Малыш'
# elif age >=4 and age < 13:
#     human = 'Ребенок'
# elif age >=13 and age < 20:
#     human = 'Подросток'
# elif age >=20 and age < 65:
#     human = 'Взрослый'
# else:
#     human = 'Пожилой'

# print(f"this human is {human}")

# favorite_fruits = ['banana', 'apple', 'pineapple']

# if 'banana' in favorite_fruits:
#     fruit = 'banana'
#     print(f"you like  is {fruit}")
# if 'apple' in favorite_fruits:
#     fruit = 'apple'
#     print(f"you like  is {fruit}")
# if 'pineapple' in favorite_fruits:
#     fruit = 'pineapple'
#     print(f"you like  is {fruit}")
# if 'pear' in favorite_fruits:
#     fruit = 'pear'
#     print(f"you like  is {fruit}")
# if 'peach' in favorite_fruits:
#     fruit = 'peach'
#     print(f"you like  is {fruit}")

# names = ['Egor', 'Andrey', 'Vlad', 'admin', 'Aleksey']

# if names:
#     for name in names:
#         if name != 'admin':
#             print(f"Hi, {name}, thanks for your helping")
#         else:
#             print(f"Hi, {name}, do you want do this")
# else:
#     print('list is empty')

# current_users = ['Egor', 'Andrey', 'Vlad', 'Sergey', 'Aleksey', 'Kirill']

# another_users = [name.lower() for name in current_users]

# print(another_users)

# new_users = ['Aleksandr', 'andrey', 'Maksim', 
#              'Nikita', 'Aleksey', 'kirill', 
#              'Leonid']

# for name in new_users:
#     if name in current_users:
#         print(f'Sorry {name} is busy')
#     elif name in another_users:
#         print(f'Sorry {name} is busy2')
#     else:
#         print(f"this name {name} is free")

inted = [i for i in range(1, 10)]

for i in inted:
    if i == 1:
        print(f'\n{i}st')
    elif i == 2:
        print(f'\n{i}nd')
    elif i == 3:
        print(f'\n{i}rd')
    else:
        print(f'\n{i}th')