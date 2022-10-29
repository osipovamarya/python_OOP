class Notebook:
    def __init__(self, custom_list):
        self._notes = custom_list

    @property
    def notes_list(self):
        for i in self._notes:
            print(f'{self._notes.index(i)+1}.{i}')


note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
note.notes_list


class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars*100+cents

    @property
    def dollars(self):
        return int(self.total_cents/100)
        # return self.total_cents // 100 целочисленное деление

    @dollars.setter
    def dollars(self, value_dol):
        if isinstance(value_dol, int) and value_dol >= 0:
            self.total_cents = value_dol*100+self.cents
        else:
            print('Error dollars')

    @property
    def cents(self):
        return int(round((self.total_cents / 100) % 1, 2) * 100)
        # return self.total_cents % 100 остаток от деления на 100

    @cents.setter
    def cents(self, value_cent):
        if isinstance(value_cent, int) and 0 <= value_cent < 100:
            self.total_cents = self.dollars*100+value_cent
        else:
            print('Error cents')

    def __str__(self):
        return f'Ваше состояние составляет {self.dollars} долларов {self.cents} центов'
