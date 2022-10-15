class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


class Laptop:
    def __init__(self, brand, model, price):
        self.brand, self.model, self.price = brand, model, price
        self.laptop_name = f'{brand} {model}'


class SoccerPlayer:
    def __init__(self, name, surname):
        self.name, self.surname = name, surname
        self.goals, self.assists = 0, 0

    def score(self, more_goals=1):
        self.goals += more_goals

    def make_assist(self, more_assist=1):
        self.assists += more_assist

    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')

class Zebra:
    def __init__(self):
        self.stripe = 'Полоска белая'
        self.count = 1

    def which_stripe(self):
        self.stripe = 'Полоска черная' if self.count % 2 == 0 else 'Полоска белая'
        print(self.stripe)
        self.count += 1

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name, self.last_name, self.age = first_name, last_name, age

    def full_name(self):
        return (f'{self.last_name} {self.first_name}')

    def is_adult(self):
        return(self.age >= 18)
