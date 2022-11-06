class Person:
    def __init__(self, name, surname, gender='male'):
        self.name, self.surname = name, surname
        if gender == 'male' or gender == 'female':
            self.gender = gender
        else:
            print('Не знаю, что вы имели ввиду? Пусть это будет мальчик!')
            self.gender = 'male'
        pass

    def __str__(self):
        return f'Гражданин {self.surname} {self.name}' if self.gender == 'male' else f'Гражданка {self.surname} {self.name}'

p1 = Person('Chuck', 'Norris')
print(p1)  # печатает "Гражданин Norris Chuck"
p2 = Person('Mila', 'Kunis', 'female')
print(p2)  # печатает "Гражданка Kunis Mila"
p3 = Person('Оби-Ван', 'Кеноби', True)  # печатает "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
print(p3)  # печатает "Гражданин Кеноби Оби-Ван"


class Vector:
    def __init__(self, *args):
        self.values = []
        for arg in args:
            if isinstance(arg, int):
                self.values.append(arg)

    def __str__(self):
        return f'Вектор({", ".join(map(str, sorted(self.values)))})' if self.values else 'Пустой вектор'

v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"
v2 = Vector()
print(v2) # печатает "Пустой вектор"
v3 = Vector('ggfhg',666,'орпро',99.08,77)
print(v3)