

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


# import random

# length = int(input('your length '))

# alf_big = [chr(i).upper() for i in range(97, 123)]
# alf_smoll = [chr(i) for i in range(97, 123)]
# digits = [str(i) for i in range(10)]

# all_chars = alf_big + alf_smoll + digits
# print(all_chars)
# password = []

# for _ in range(length):
#     password.append(random.choice(all_chars))

# print(password)
# # Преобразуем список в строку и выводим
# password_str = ''.join(password)
# print('Ваш пароль:', password_str)

# import random

# a = random.randint(1, 100)
# count = 0

# print('Я загадал число от 1 до 100. Угадай!')

# while True:
#     try:
#         b = int(input('Твоя попытка: '))
#         count += 1
#         if b == a:
#             print('Угадал!')
#             print(f'Число попыток: {count}')
#             break
#         elif b < a:
#             print('Моё число больше.')
#         else:
#             print('Моё число меньше.')
#     except ValueError:
#         print('Ошибка: введи число!')

# def is_prime(n):
#     if n <= 1:  
#         return False  
#     for i in range(2, int(n**0.5) + 1):  
#         if n % i == 0:  
#             return False   
#     return True  

# num = int(input('Your number: '))
# if is_prime(num):
#     print(f'Number {num} is prime')
# else:
#     print(f'Number {num} is not prime')

# def sort_words(text):
#     sorts = []
#     word = ''
#     for i in text:
#         if i == ' ':
#             if word:
#                 sorts.append(word)
#             word = ''
#         else:
#             word += i
# # Сортировка: сначала по длине, потом по алфавиту
#     sorted_words = sorted(sorts, key=lambda x: (len(x), x))
#     return sorted_words

# def sort_words(text):
#     words = text.split()  # Разбивает строку по пробелам
#     return sorted(words, key=lambda x: (len(x), x))

# text = input('Введи текст: ')
# result = sort_words(text)
# print('Результат:', result)

def words(text):
    word = text.split('-')
    print(word)
words('1-2-3-4')

# numbers = [10, 15, 7, 3, 12]
lists = ['кот', 'пёс', 'слон', 'мышь']
sorted_numbers = sorted(lists, key=lambda x: x[-1])
print(sorted_numbers)