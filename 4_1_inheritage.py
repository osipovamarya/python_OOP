class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name, self.max_speed, self.mileage = name, max_speed, mileage

    def display_info(self):
        print(f'Vehicle Name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}')

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

class Boat(Vehicle):
    pass

class RaceCar(Car):
    pass


class Person:
    def __init__(self, name):
        self.name= name

    def get_name(self):
        return self.name

    def is_employee(self):
        return False

class Employee(Person):
    def is_employee(self):
        return True


