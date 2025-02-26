# class Dog:
#     """Простая модель собаки"""

#     def __init__(self, name, age):
#         """Инициализация атрибутов"""
#         self.name = name
#         self.age = age
    
#     def sit(self):
#         print(f'{self.name} if now sitting')

#     def roll_over(self):
#         print(f'{self.name} rolled over')


# my_dog = Dog('alpha', 6)
# print(my_dog.age)
# my_dog.sit()

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'{self.restaurant_name}, {self.cuisine_type}')
        
    
    def open_restaurant(self):
        print(f'Restaurant {self.restaurant_name} is open')

rest = Restaurant('Peperoni', 'god')

rest.describe_restaurant()
rest.open_restaurant()