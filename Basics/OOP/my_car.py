from car import Car
from electrik_car import ElectrickCar
from Dog import Restaurant

my_new_car = Car('honda', 'accord', '2010')
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_leaf = ElectrickCar('honda', 'accc', 2015)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

mustang = Car('ford', 'mustang', 2018)
print(mustang.get_descriptive_name())

rest = Restaurant('mango', 'fgo')
rest.describe_restaurant()