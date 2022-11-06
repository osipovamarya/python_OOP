from string import digits, ascii_letters


class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login):
        if '@' not in login:
            raise ValueError("Логин должен содержать один символ '@'")
        if '.' not in login.split('@')[1]:
            raise ValueError("Логин должен содержать символ '.'")
        else:
            self.__login = login

    @property
    def password(self):
        return self.__password

    @staticmethod
    def is_include_digit(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @staticmethod
    def is_include_all_register(password):
        for i in password:
            if i.isupper() and not password.isupper():
                return True
        return False

    @staticmethod
    def is_include_only_latin(password):
        for i in password:
            if i not in ascii_letters and i not in digits:
                return False
        return True

    @staticmethod
    def check_password_dictionary(password):
        with open('easy_passwords.txt', 'r') as p:
            lines = p.readlines()
        for line in lines:
            if password == line.rstrip():
                p.close()
                return True
        p.close()
        return False

    @password.setter
    def password(self, password):
        if not isinstance(password, str):
            raise TypeError("Пароль должен быть строкой")
        if not 4 < len(password) < 12:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not Registration.is_include_digit(password):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if not Registration.is_include_all_register(password):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        if not Registration.is_include_only_latin(password):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        if Registration.check_password_dictionary(password):
            raise ValueError('Ваш пароль содержится в списке самых легких')
        self.__password = password


class File:
    def __init__(self, name):
        self.name = name
        self.in_trash = False
        self.is_deleted = False

    def restore_from_trash(self):
        print(f'Файл {self.name} восстановлен из корзины')
        self.in_trash = False

    def remove(self):
        print(f'Файл {self.name} был удален')
        self.is_deleted = True

    def read(self):
        if self.is_deleted:
            print(f'ErrorReadFileDeleted({self.name})')
            return
        if self.in_trash:
            print(f'ErrorReadFileTrashed({self.name})')
            return
        print(f'Прочитали все содержимое файла {self.name}')

    def write(self, content):
        if self.is_deleted:
            print(f'ErrorWriteFileDeleted({self.name})')
            return
        if self.in_trash:
            print(f'ErrorWriteFileTrashed({self.name})')
            return
        print(f'Записали значение {content} в файл {self.name}')


class Trash:
    content = []

    @staticmethod
    def add(file):
        if isinstance(file, File):
            file.in_trash = True
            Trash.content.append(file)
        else:
            print('В корзину добавлять можно только файл')

    @staticmethod
    def clear():
        print('Очищаем корзину')
        for f in Trash.content:
            f.remove()
        Trash.content = []
        print('Корзина пуста')

    @staticmethod
    def restore():
        print('Восстанавливаем файлы из корзины')
        for f in Trash.content:
            f.restore_from_trash()
        Trash.content = []
        print('Корзина пуста')
