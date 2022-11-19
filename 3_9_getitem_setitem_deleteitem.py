class Building:
    def __init__(self, floors):
        self.floors = floors
        self.booking = dict.fromkeys(range(self.floors), None)

    def __setitem__(self, key, value):
        if 0 <= key <= self.floors:
            self.booking[key] = value
        else:
            raise IndexError('Нет такого этажа')

    def __getitem__(self, item):
        if 0 <= item <= self.floors:
            return self.booking[item]
        else:
            raise IndexError('Нет такого этажа')

    def __delitem__(self, key):
        if 0 <= key <= self.floors:
            self.booking[key] = None
        else:
            raise IndexError('Нет такого этажа')



iron_building = Building(22)  # Создаем здание с 22 этажами
iron_building[0] = 'Reception'
iron_building[1] = 'Oscorp Industries'
iron_building[2] = 'Stark Industries'
print(iron_building[2])
del iron_building[2]
print(iron_building[2])