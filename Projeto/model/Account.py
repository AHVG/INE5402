import model.Element


class Account(model.Element.Element):

    def __init__(self, user, password):
        super().__init__()
        self.user = user
        self.password = password

    def set_user(self, user):
        self.user = user

    def get_user(self):
        return self.user

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def __eq__(self, other):
        if self.get_user() == other.get_user() and self.get_password() == other.get_password():
            return True
        return False


def show_account(account):
    user = account.get_user()
    password = account.get_password()
    print()
    print(f"User: {user}")
    print(f"Password: {password}")
    print()