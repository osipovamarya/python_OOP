class User:
    def __init__(self, n, r):
        self.name, self.role = n, r


class Access:

    __access_list = ['admin', 'developer']

    @staticmethod
    def __check_access(r):
        return True if r in Access.__access_list else False

    @staticmethod
    def get_access(user):
        if isinstance(user, User) or type(object).__name__ == 'Point':
            print(f'User {user.name}: success') if Access.__check_access(user.role) else print('AccessDenied')
        else:
            print('AccessTypeError')
