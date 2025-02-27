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

class Car:
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        print(f'this car has {self.odometer_reading} miles on it')

    def update_odometr(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You cant roll back an odometr')

    def increment_odometr(self, miles):
        self.odometer_reading += miles

        
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'{self.restaurant_name}, {self.cuisine_type}')
        
    def open_restaurant(self):
        print(f'Restaurant {self.restaurant_name}' + 
              f'is open and {self.number_served}')

    def set_number_served(self, people):
        self.number_served = people
        print(f'Peoples is {self.number_served}')

    def increment_number_served(self, people):
        self.number_served += people
        print(f'Peoples on days is {self.number_served}')


# rest = Restaurant('Peperoni', 'god')

# # rest.describe_restaurant()
# rest.open_restaurant()
# rest.number_served = 2
# rest.open_restaurant()
# rest.set_number_served(3)
# rest.increment_number_served(6)
# rest.increment_number_served(9)

# rest2 = Restaurant('Monan', 'not', 3)

# rest2.describe_restaurant()
# rest2.open_restaurant()

class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = 0

    def defdescribe_user(self):
        print(f'User {self.first_name} {self.last_name},'+
              f'year is {self.age} and live in {self.city}')

    def greet_user(self):
        print(f'hello {self.first_name}')

    def increment_login_attempts(self, login):
        self.login_attempts+=login
        print(f'Peoples in system is {self.login_attempts}')

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'Peoples in system is {self.login_attempts}')

class Admin(User):
    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.priviliges = Priviliges()

    def priviliges_admin(self):
        print(f'Admin can {self.priviliges}')

class Priviliges:
    def __init__(self):
        self.priviliges = ['разрешено добавлять сообщения',
                            'разрешено удалять пользователей',
                              'разрешено банить пользователей']

    def priviliges_admin(self):
        print(f'Admin can {self.priviliges}')

# priv = Admin('Egor', 'Andryyichuk', 35, 'St.Petersburg')
# priv.priviliges.priviliges_admin()


# priv.defdescribe_user()
# us = User('Egor', 'Andryyichuk', 35, 'St.Petersburg')
# us2 = User('Aleksey', 'Alekseev', 27, 'Tumen')
# us.increment_login_attempts(2)
# us.increment_login_attempts(2)
# us.reset_login_attempts()
# us.defdescribe_user()
# us.greet_user()
# us2.defdescribe_user()
# us2.greet_user()


class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['banana', 'mango', 'apple']

    def our_flovars(self):
        print(f'We have {self.flavors}')

# ice = IceCreamStand('IceCream', 'Cff')

# ice.our_flovars()