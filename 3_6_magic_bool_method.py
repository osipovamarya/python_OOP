class City:
    def __init__(self, name):
        self.name = name.title()

    def __str__(self):
        return self.name

    def __bool__(self):
        return not self.name[-1] in 'aeiou'


p1 = City('new york')
print(p1)  # печатает "New York"
print(bool(p1))  # печатает "True"
p2 = City('SaN frANCISco')
print(p2)  # печатает "San Francisco"
print(p2 == True)  # печатает "False"


class Quadrilateral:
    def __init__(self, width, height=None):
        self.width, self.height = width, height if height else width

    def __str__(self):
        return f'Куб размером {self.width}х{self.height}' if self else f'Прямоугольник размером {self.width}х{self.height}'

    def __bool__(self):
        return self.width == self.height

