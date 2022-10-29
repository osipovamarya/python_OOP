class Square:
    def __init__(self, side):
        self.__side__ = side
        self.__perimeter__ = None

    @property
    def side(self):
        return self.__side__

    @side.setter
    def side(self, value):
        self.__side__ = value
        self.__perimeter__ = None

    @property
    def perimeter(self):
        if self.__perimeter__ is None:
            self.__perimeter__ = self.side * 4
        return self.__perimeter__


class Rectangle:
    def __init__(self, h, w):
        self.height = h
        self.weight = w

    @property
    def area(self):
        return self.height*self.weight


class Date:
    def __init__(self, d, m, y):
        self.day = f'0{d}' if d % 10 == d else d
        self.month = f'0{m}' if m % 10 == m else m
        if y % 1000 != y:
            self.year = y
        elif y % 100 != y:
            self.year = f'0{y}'
        elif y % 10 != y:
            self.year = f'00{y}'
        else: self.year = f'000{y}'

    @property
    def date(self):
        return f'{self.day}/{self.month}/{self.year}'

    @property
    def usa_date(self):
        return f'{self.month}-{self.day}-{self.year}'