class Person:
    def __init__(self, name, passport):
        self.name, self.passport = name, passport

    def display(self):
        print(f'{self.name}: {self.passport}')


class Employee(Person):
    def __init__(self, name, passport, salary, department):
        super(Employee, self).__init__(name, passport)
        self.salary, self.department = salary, department


a = Employee('Raul', 886012, 200000, "QA")

a.display()


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name, self.mileage, self.capacity = name, mileage, capacity

    def fare(self):
        return self.capacity * 100

    def display(self):
        print(f'Total {self.name} fare is: {self.fare()}')


class Bus(Vehicle):
    def __init__(self, name, mileage):
        super(Bus, self).__init__(name, mileage, 50)

    def fare(self):
        return super(Bus, self).fare() + super(Bus, self).fare() * 0.1


class Taxi(Bus):
    def __init__(self, name, mileage):
        super(Bus, self).__init__(name, mileage, 4)

    def fare(self):
        return super(Bus, self).fare() + super(Bus, self).fare() * 0.35


sc = Vehicle('Scooter', 100, 2)
sc.display()

merc = Bus("Mercedes", 120000)
merc.display()

polo = Taxi("Volkswagen Polo", 15000)
polo.display()