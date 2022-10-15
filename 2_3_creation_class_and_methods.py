class Dog:
    def __init__(self, name, age):
        self.name, self.age = name, age

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        return f'{self.name} says {sound}'


class Stack:
    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def pop(self):
        return self.values.pop() if not self.is_empty() else print('Empty Stack')

    def peek(self):
        if self.is_empty():
            print('Empty Stack')
            return None
        else:
            return self.values[-1]

    def is_empty(self):
        return True if not self.values else False

    def size(self):
        return len(self.values)


persons = [
    ('Allison Hill', 334053, 'M', '1635644202'),
    ('Megan Mcclain', 191161, 'F', '2101101595'),
    ('Brandon Hall', 731262, 'M', '6054749119'),
    ('Michelle Miles', 539898, 'M', '1355368461'),
    ('Donald Booth', 895667, 'M', '7736670978'),
    ('Gina Moore', 900581, 'F', '7018476624'),
    ('James Howard', 460663, 'F', '5461900982'),
    ('Monica Herrera', 496922, 'M', '2955495768'),
    ('Sandra Montgomery', 479201, 'M', '5111859731'),
    ('Amber Perez', 403445, 'M', '0602870126')
]


class Worker:
    def __init__(self, name, salary, gender, passport):
        self.name, self.salary, self.gender, self.passport = name, salary, gender, passport

    def get_info(self):
        print(f'Worker {self.name}; passport-{self.passport}')


worker_objects = []

for p in persons:
    w = Worker(p[0], p[1], p[2], p[3])
    worker_objects.append(w)

for o in worker_objects:
    o.get_info()

# пример решения с распаковкой кортежа worker_objects = [Worker(*i) for i in persons]


class CustomLabel:
    def __init__(self, text, **kwargs):
        self.text = text
        for key, value in kwargs.items():
            setattr(self, key, value)

    def config(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)



class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age

    def display_person_info(self):
        print(f'Person: {self.name}, {self.age}')


class Company:
    def __init__(self, company_name, location):
        self.company_name, self.location = company_name, location

    def display_company_info(self):
        print(f'Company: {self.company_name}, {self.location}')


class Employee:
    def __init__(self, name, age, company_name, location):
        self.personal_data = Person(name, age)
        self.work = Company(company_name, location)

