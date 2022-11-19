class Addition:
    def __call__(self, *args, **kwargs):
        values = []
        for i in args:
            if isinstance(i, (int, float)):
                values.append(i)
        print(f'Сумма переданных значений = {sum(values)}')


add = Addition()

add(10, 20) # печатает "Сумма переданных значений = 30"
add(1, 2, 3.4) # печатает "Сумма переданных значений = 6.4"
add(1, 2, 'hello', [1, 2], 3) # печатает "Сумма переданных значений = 6"

import time

class Timer:
    def __init__(self, func):
        self.fun = func

    def __call__(self, *args, **kwargs):
        self.start = time.time()
        self.fun()
        self.finish = time.time()
        print(f'Время работы программы {self.finish - self.start}')


@Timer
def calculate():
    for i in range(10000000):
        2**100

calculate()