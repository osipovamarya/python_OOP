class PowerTwo:
    def __init__(self, iterto):
        self.iterto = iterto

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index > self.iterto:
            raise StopIteration
        count = 2**self.index
        self.index += 1
        return count



numbers = PowerTwo(2)

iterator = iter(numbers)

print(next(iterator)) # печатает 1
print(next(iterator)) # печатает 2
print(next(iterator)) # печатает 4
print(next(iterator)) # исключение StopIteration



class InfinityIterator:

    def __iter__(self):
        self.num = 0
        self.index = 0
        return self

    def __next__(self):
        self.num = self.num*0 + self.index
        self.index += 10
        return self.num
