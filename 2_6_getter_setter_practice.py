class UserMail:
    def __init__(self, login, email):
        self.login, self.__email = login, email

    def get_email(self):
        return self.__email

    def set_email(self, value):
        if isinstance(value, str) and len(value.split('@')) == 2 and '.' in value.split('@')[1]:
            self.__email = value
        else:
            print(f'ErrorMail:{value}')

    email = property(fget=get_email, fset=set_email)


k = UserMail('belosnezhka', 'prince@wait.you')
print(k.email)  # prince@wait.you
k.email = [1, 2, 3]  # ErrorMail:[1, 2, 3]
k.email = 'prince@still@.wait'  # ErrorMail:prince@still@.wait
k.email = 'prince@stillwait' # ErrorMail:prince@stillwait
k.email = 'prince@still.wait'
print(k.email)  # prince@still.wait
