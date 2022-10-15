class Lion:

    def roar(self):
        print('Rrrrrrr!!!')


class Robot:
    def say_hello(self):
        print('Hello, human! My name is ' + self.name) if hasattr(self, 'name') else print('У робота нет имени')
    def say_bye(self):
        print('See u later alligator')
    def set_name(self, name):
        self.name = name


class Counter:
    def start_from(self, start=0):
        self.x = start

    def increment(self):
        self.x += 1

    def display(self):
        print(f'Текущее значение счетчика = {self.x}')

    def reset(self):
        self.x = 0

class Constructor:
    def add_atribute(self, name, value):
        setattr(self, name, value)

    def display(self):
        print(self.__dict__)

class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, object):
        return ((self.x - object.x)**2 + (self.y - object.y)**2)**0.5 if type(object).__name__ == 'Point' else print('Передана не точка')