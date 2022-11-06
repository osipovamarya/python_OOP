class Vector:
    def __init__(self, *args):
        self.values = []
        for arg in args:
            if isinstance(arg, int):
                self.values.append(arg)
                self.values.sort()

    def __str__(self):
        return f'Вектор({", ".join(map(str, sorted(self.values)))})' if self.values else 'Пустой вектор'

    def __add__(self, other):
        if isinstance(other, int):
            new_values = []
            for i in self.values:
                new_values.append(i+other)
            return Vector(*new_values)

        elif isinstance(other, Vector):
            if len(other.values) == len(self.values):
                new_values = []
                for i in range(len(self.values)):
                    new_values.append(other.values[i] + self.values[i])
                return Vector(*new_values)
            else:
                return 'Сложение векторов разной длины недопустимо'
        else:
            print(f'Вектор нельзя сложить с {other}')

    def __mul__(self, other):
        if isinstance(other, int):
            new_values = []
            for i in self.values:
                new_values.append(i*other)
            return Vector(*new_values)

        elif isinstance(other, Vector):
            if len(other.values) == len(self.values):
                new_values = []
                for i in range(len(self.values)):
                    new_values.append(other.values[i] * self.values[i])
                return Vector(*new_values)
            else:
                return 'Умножение векторов разной длины недопустимо'
        else:
            print(f'Вектор нельзя умножать с {other}')

v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"

v2 = Vector(3,4,5)
print(v2) # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3) # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4) # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print(v5) # печатает "Вектор(2, 4, 6)"
v5 + 'hi' # печатает "Вектор нельзя сложить с hi"