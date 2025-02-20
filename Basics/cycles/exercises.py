# pizzas = ['margarita', 'four cheez', 'diablo']

# for pizza in pizzas:
#     print(f'{pizza.title()} is my favorite pizza')
# print('i love pizza')

# animals = ['cat', 'tiger', 'lion']

# for animal in animals:
#     print(f'{animal.title()} have a big claws')

# print('Ani animals is good')

# for value in range(1, 21, 2):
#     print(value)

# for value in range(3, 30, 3):
#     print(value)

# million = list(range(1, 100_000_1))

# print(max(million))
# print(min(million))
# print(sum(million))

# for i in million:
    # print(i)


million = list(range(1, 11))
for i in million:
    print(i**3)

million = [i**3 for i in range(1, 11)]
print(million)