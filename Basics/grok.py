import random

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

# def words(text):
#     word = text.split('-')
#     print(word)
# words('1-2-3-4')

# # numbers = [10, 15, 7, 3, 12]
# lists = ['кот', 'пёс', 'слон', 'мышь']
# sorted_numbers = sorted(lists, key=lambda x: x[-1])
# print(sorted_numbers)

# a = 0
# b = random.randint(1, 100)
# attempts =  0


# while a != b:
#     a = input('Your number is ')
#     attempts += 1
#     if a < b:
#         print('So smoll')
#         attempts+=1
#     elif a > b:
#         print('So big')
#         attempts+=1
#     else:
#         print(f'You win in the {attempts} times')


# def main():
#     number = random.randint(1, 100)
#     guesses = 0
#     while True:
#         guess = int(input("Угадай число (1-100): "))
#         guesses += 1
#         if guess == number:
#             print(f"Поздравляю! Ты угадал за {guesses} попыток.")
#             break
#         elif guess < number:
#             print("Слишком низко. Попробуй ещё.")
#         else:
#             print("Слишком высоко. Попробуй ещё.")

# if __name__ == "__main__":
#     main()

# shops = ['milk', 'bread', 'apple', 'tomato']

# while True:
#     try:
#         print(f'Менеджер списка покупок:\n1. Добавить товар\n2. Удалить товар\n3. Просмотреть список\n4. Выйти\n')
#         a = int(input('Выберите действие (1-4): '))
#         if a == 1:
#             b = input('Что хотите добавить? ')
#             shops.append(b)
#             print(f'{b} добавлен в список.')
#         elif a == 2:
#             b = input('Что хотите удалить? ')
#             if b in shops:
#                 shops.remove(b)
#                 print(f'{b} удалён из списка.')
#             else:
#                 print(f'{b} нет в списке.')
#         elif a == 3:
#             if shops:
#                 print('Список покупок:', shops)
#             else:
#                 print('Список пуст.')
#         elif a == 4:
#             print('До свидания!')
#             break
#         else:
#             print('Нет такого номера в менеджере.')
#     except ValueError:
#         print('Введите пожалуйста число.')


# Задание 1: Генератор викторины
# Создай программу, которая генерирует простую викторину с вопросами и ответами. Программа должна:

# Хранить вопросы и правильные ответы в словаре (например, {"2 + 2": 4, "5 * 3": 15}).
# Случайно выбирать 5 вопросов из словаря.
# Запрашивать у пользователя ответы и проверять их.
# В конце вывести количество правильных ответов и процент успеха.
# Пример вывода:
# text
# Перенос
# Копировать
# Вопрос 1: 2 + 2 = ?
# Твой ответ: 4
# Правильно!
# Вопрос 2: 5 * 3 = ?
# Твой ответ: 12
# Неправильно. Правильный ответ: 15
# ...
# Результат: 3 из 5 правильных (60%)
# Задание 2: Сортировщик списка
# Напиши программу, которая позволяет пользователю ввести список чисел, а затем сортирует его одним из двух способов: по возрастанию или по убыванию. Используй меню для выбора действия.

# Требования:
# Запроси у пользователя числа через ввод строки (например, "1 2 3 4 5") и преобразуй их в список.
# Покажи меню с опциями: 1) Сортировать по возрастанию, 2) Сортировать по убыванию, 3) Выйти.
# Выведи отсортированный список после выбора.
# Пример вывода:
# text
# Перенос
# Копировать
# Введи числа через пробел: 5 2 8 1 9
# 1. Сортировать по возрастанию
# 2. Сортировать по убыванию
# 3. Выйти
# Выбери действие (1-3): 1
# Отсортированный список: [1, 2, 5, 8, 9]

# Подсказки
# Задание 1: Используй random.choice() или random.sample() для выбора вопросов. Словарь удобно хранит пары "вопрос-ответ".
# Задание 2: Разбери строку ввода с помощью split() и преобразуй в числа. Для сортировки используй sorted() с параметром reverse.
# Задание 3: В классе храни атрибуты через self, а для управления задачами можешь использовать список объектов класса.


# def vibor(quest, qu):
#     quests = []
#     for i in quest:
#         quests.append(i)
#     rand = random.sample(quests, qu)
#     return rand
#     # return random.sample(list(quest.keys()), qu)

# def variant(rand, quest):
#     attempts = 0
#     for i in rand:
#         try:
#             b = int(input(f'Вопрос: {i} и твой ответ : '))
#             for k, v in quest.items():
#                 if i == k:
#                     if b == v:
#                         print('Правильный ответ')
#                         attempts+=1
#                     else:
#                         print('Это не правильный ответ')
            
#             # if b == quest[i]:
#             #     print('Правильный ответ')
#             #     attempts += 1
#             # else:
#             #     print('Это не правильный ответ')
#         except ValueError:
#             print(print('Введи число!'))
#     return attempts

# def win(attempts, qu):
#     proc = attempts / qu * 100
#     return proc

# def main():
#     quest = {
#         '2 + 2': 4,
#         '12 * 4': 48,
#         '10 / 5': 2,
#         '125 / 5': 25,
#         '3 * 17': 51,
#         '6 * 7': 42,
#         '5 * 13': 65,
#         '20 * 7': 140,
#     }
#     qu = 5
#     rand = vibor(quest, qu)
#     attempts = variant(rand, quest)
#     c = win(attempts, qu)
#     print(f'You win {attempts} quests and you proc {c}')

# if __name__ == "__main__":
#     main()

# def numb():
#     try:
#         num_list = [int(i) for i in list(input('список чисел: ').split())]
#     except ValueError:
#         print('Введите цифры')
#     return num_list

# def sort_des(lists):
#     sort_list = sorted(lists)
#     return sort_list

# def sort_ascen(lists):
#     sort_list = sorted(lists, reverse=True)
#     return sort_list

# def main():
#     lists = numb()
#     print(f'Сортировщик списка:\n1. Сортировать по возрастанию\n2 Сортировать по убыванию\n3. Выйти\n')
#     while True:
#         menu = int(input('Выбери что будем делать?\n'))
#         if menu == 1:
#             print('Сортируем список по возрастанию')
#             print(sort_des(lists))
#         elif menu == 2:
#             print('Сортируем список по убыванию')
#             print(sort_ascen(lists))
#         elif menu == 3:
#             print('Выходим')
#             break

# if __name__ == "__main__":
#     main()


# Задание 3: Таймер задач
# Создай класс TaskTimer, который помогает отслеживать время, потраченное на задачи. Программа должна:

# Иметь класс с атрибутами: название задачи и общее время выполнения (в минутах).
# Метод для добавления времени (например, "добавить 10 минут").
# Метод для вывода текущего состояния задачи.
# В основной программе создать несколько задач и управлять ими через меню.
# Пример вывода:
# text
# Перенос
# Копировать
# Меню таймера задач:
# 1. Добавить время к задаче
# 2. Показать состояние задач
# 3. Выйти
# Выбери действие (1-3): 1
# Выбери задачу (1 - Учёба, 2 - Работа): 1
# Сколько минут добавить? 15
# Время для "Учёба" обновлено.
# Выбери действие (1-3): 2
# Учёба: 15 минут
# Работа: 0 минут


class TaskTimer:
    def __init__(self, task, time_on_task=0):
        self.task = task
        self.time_on_task = time_on_task

    def add_time(self, time):
        if time > 0:
            self.time_on_task += time
            print(f"Добавлено {time} минут к задаче '{self.task}'")
        else:
            print("Время должно быть положительным")

    def show_status(self):
        print(f"{self.task}: {self.time_on_task} минут")

def main():
    tasks = [
        TaskTimer('Работа', 30),
        TaskTimer('Учеба', 50)
    ]
    while True:
        try:
            print('Меню таймера задач:\n1. Добавить время к задаче\n2. Показать состояние задач\n3. Выйти')
            choice = int(input('Выбери действие (1-3): '))
            if choice == 1:
                task_num = int(input(f'Выбери задачу (1 - {tasks[0].task}, 2 - {tasks[1].task}): '))
                if task_num in [1, 2]:
                    time = int(input('Сколько времени добавить? '))
                    tasks[task_num - 1].add_time(time)
                else:
                    print('Выбери 1 или 2')
            elif choice == 2:
                print('Состояние задач:')
                for task in tasks:
                    task.show_status()
            elif choice == 3:
                print('Выходим из программы')
                break
            else:
                print('Выбери от 1 до 3')
        except ValueError:
            print('Нужно ввести число')

if __name__ == "__main__":
    main()
