class Student:
    def __init__(self, name, age, branch):
        self.__name, self.__age, self.__branch = name, age, branch

    def __display_details(self):
        print(f'Имя: {self.__name}\n'
              f'Возраст: {self.__age}\n'
              f'Направление: {self.__branch}')

    def access_private_method(self):
        self.__display_details()


obj = Student("Adam Smith", 25, "Information Technology")
obj.access_private_method()
