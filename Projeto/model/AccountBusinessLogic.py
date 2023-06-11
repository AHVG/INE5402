import model.Account


def create_account_by_form(account_form):
    fields = account_form.get_fields()
    return model.Account.Account(fields['user'].get_value(), fields['password'].get_value())


def is_account_valid(user, password):
    if " " not in user and " " not in password:
        return True
    return False


class AccountBusinessLogic:

    def __init__(self, repository):
        self.repository = repository

    def account_exist(self, account):
        accounts = self.get_all()
        for other in accounts:
            if other == account:
                return True
        return False

    def add(self, account):
        if self.account_exist(account):
            return False
        self.repository.add(account)
        return True

    def delete_by_id(self, id):
        return self.repository.delete_by_id(id)

    def update(self, older_account, new_account):
        return self.repository.update(older_account, new_account)

    def get_by_id(self, id):
        return self.repository.get_by_id(id)

    def get_all(self):
        return self.repository.get_all()

    def download(self):
        self.repository.download()

    def upload(self):
        self.repository.upload()
