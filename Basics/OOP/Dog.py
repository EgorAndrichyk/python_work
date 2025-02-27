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

# class Restaurant:

#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         print(f'{self.restaurant_name}, {self.cuisine_type}')
        
    
#     def open_restaurant(self):
#         print(f'Restaurant {self.restaurant_name} is open')

# rest = Restaurant('Peperoni', 'god')

# rest.describe_restaurant()
# rest.open_restaurant()
# rest2 = Restaurant('Monan', 'not')

# rest2.describe_restaurant()
# rest2.open_restaurant()

class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def defdescribe_user(self):
        print(f'User {self.first_name} {self.last_name}, year is {self.age} and live in {self.city}')

    def greet_user(self):
        print(f'hello {self.first_name}')

us = User('Egor', 'Andryyichuk', 35, 'St.Petersburg')
us2 = User('Aleksey', 'Alekseev', 27, 'Tumen')

us.defdescribe_user()
us.greet_user()
us2.defdescribe_user()
us2.greet_user()