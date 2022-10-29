import os
import hashlib

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

person = Person('Jack', 33)

# Считываем значения
# person.name
# Jack
# person.age
# 33

# Пытаемся записать новое значение
# person.age = 42
# Traceback (most recent call last):
#     ...
# AttributeError: can't set attribute

# при этом вызов person._age = 42 сработает


class Square:
    def __init__(self, side):
        self.side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = float(value)

    @property
    def area(self):
        return self.side ** 2

    @area.setter
    def area(self, value):
        self.side = value ** 0.5


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @property
    def password(self):
        raise AttributeError("Пароль можно только менять, нельзя смотреть")

    @password.setter
    def password(self, plaintext):
        salt = os.urandom(32)
        self._hashed_password = hashlib.pbkdf2_hmac(
            "sha256", plaintext.encode("utf-8"), salt, 100_000
        )


# >>> jack = User("Jack", "secret_key")
#
# >>> jack._hashed_password
# b'7\x1f+\x02\xc4q\x93\xb6\x98\xb3\r\x9f\x9e\xa4v\nI\xde\x10\x11\x98\xb7\xcf\xff\x9c\x83f\xe4\x07\x8c\xce\xc8'
#
# >>> jack.password
# Traceback (most recent call last):
# ...
#   raise AttributeError("Пароль можно только менять, нельзя смотреть")
#
# >>> jack.password = "new_secret"
#
# >>> jack._hashed_password
# b'H\xd3f\xe5\x92,\xc4\xe6\xf29g\xe0\x96I\xd1\xf3^\xd6D\xb4\xbd\x89\xc8\x85s\x13\xa6YA\x08\x89\x89'