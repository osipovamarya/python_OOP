class Robot:
    global population
    population = 0

    def __init__(self, name):
        self.name = name
        print(f'Робот {self.name} был создан')
        global population
        population += 1

    def destroy(self):
        print(f'Робот {self.name} был уничтожен')
        global population
        population -= 1

    def say_hello(self):
        print(f'Робот {self.name} приветствует тебя, особь человеческого рода')

    @classmethod
    def how_many(cls):
        global population
        print(f'{population}, вот сколько нас еще осталось')

