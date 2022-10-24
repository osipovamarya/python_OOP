class BankAccount:

    # def __init__(self, input_name, input_balance, input_passport):
    #     self.name = input_name
    #     self.balance = input_balance
    #     self.passport = input_passport

    def __init__(self, input_name, input_balance, input_passport):
        self._name = input_name         # нижним подчеркиванием указываем
        self._balance = input_balance   # что атрибут должен быть защищен
        self._passport = input_passport # от публичного доступа

    # def __init__(self, name, balance, passport):
    #     self.__name = name
    #     self.__balance = balance
    #     self.__passport = passport

    def print_data(self):   # эти данные доступны из общих вызовов
        print(self.name, self.balance, self.passport)

    def print_protected_data(self):
        print(self._name, self._balance, self._passport)

    def print_private_data(self):
        return self.__name, self.__balance, self.__passport

    def public_call(self):
      print('work public method')
      self.__print_private_data()

    def __print_private_data(self):
      print('work private method')
      print(self.__name, self.__balance, self.__passport)


account1 = BankAccount('Bob', 100000, 45484564654)
account1.print_data()
print(account1.name)
print(account1.balance)
print(account1.passport)

account1.print_protected_data()
print(account1._name)
print(account1._balance)
print(account1._passport)

print(account1.print_private_data())
print(account1.__name) # AttributeError
print(account1.__balance) # AttributeError
print(account1.__passport)# AttributeError

print(account1._BankAccount__balance) # отработает несмотря на то что пайчарм ругается
print(account1._BankAccount__name) # отработает несмотря на то что пайчарм ругается
print(account1._BankAccount__passport) # отработает несмотря на то что пайчарм ругается
account1._BankAccount__print_private_data() # отработает несмотря на то что пайчарм ругается