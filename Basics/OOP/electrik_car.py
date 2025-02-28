from car import Car

class Battery:

    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'this {self.battery_size} on kWh battery')

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        
        print(f'this car {range} miles on a full charge')

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65


class ElectrickCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

        

