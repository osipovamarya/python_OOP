from collections import defaultdict

class Product:
    def __init__(self, name, price):
        self.name, self.price = name, price

class User:
    def __init__(self, login, balance=0):
        self.login, self.balance = login, balance

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.__balance}'

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def deposit(self, value):
        self.__balance += value

    def payment(self, value):
        if self.__balance < value:
            print('Не хватает средств на балансе. Пополните счет')
            return False
        else:
            self.__balance -= value
            return True


class Cart:
    def __init__(self, user: User):
        self.user = user
        self.goods = defaultdict(int)
        self.__total = 0

    def add(self, product: Product, quantity=1):
        self.goods[product] += quantity
        self.__total += product.price * quantity

    def remove(self, product: Product, quantity=1):
        if quantity >= self.goods[product]:
            self.__total -= self.goods[product] * product.price
            self.goods.pop(product)
        else:
            self.goods[product] -= quantity
            self.__total -= product.price * quantity

    @property
    def total(self):
        return self.__total

    def order(self):
        print('Заказ оплачен') if self.user.payment(self.total) else print('Проблема с оплатой')

    def print_check(self):
        print('---Your check---')
        for p, q in sorted(self.goods.items(), key=lambda x: x[0].name):
            print(p.name, p.price, q, p.price*q)
        print(f'---Total: {self.total}---')

billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user) # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
# ''' Печатает текст ниже
# ---Your check---
# carrot 30 1 30
# lemon 20 2 40
# ---Total: 70---'''
cart_billy.add(lemon, 3)
cart_billy.print_check()
# ''' Печатает текст ниже
# ---Your check---
# carrot 30 1 30
# lemon 20 5 100
# ---Total: 130---'''
cart_billy.remove(lemon, 6)
cart_billy.print_check()
# ''' Печатает текст ниже
# ---Your check---
# carrot 30 1 30
# ---Total: 30---'''
print(cart_billy.total) # 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
# ''' Печатает текст ниже
# ---Your check---
# carrot 30 1 30
# lemon 20 5 100
# ---Total: 130---'''
cart_billy.order()
# ''' Печатает текст ниже
# Не хватает средств на балансе. Пополните счет
# Проблема с оплатой'''
cart_billy.user.deposit(150)
cart_billy.order() # Заказ оплачен
print(cart_billy.user.balance) # 20

