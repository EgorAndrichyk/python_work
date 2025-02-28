"""Класс для представления автомобиля"""

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

