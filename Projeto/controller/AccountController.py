import model.AccountBusinessLogic


class AccountController:

    def __init__(self, _model):
        self.model = _model

    def account_exist(self, account_form, response):
        account = model.AccountBusinessLogic.create_account_by_form(account_form)
        if self.model.account_exist(account):
            response.set_value(account.get_user())
            return True
        response.set_value("Login invalido")
        return False

    def add(self, account_form, response):
        account = model.AccountBusinessLogic.create_account_by_form(account_form)
        if self.model.add(account):
            response.set_value("Conta adicionado com sucesso")
        else:
            response.set_value("Usuario ou senha invalidos")

    def delete_by_id(self, id_form, response):
        response.set_value("Falha ao deletar")
        if self.model.delete_by_id(id_form.get_fields()['id']):
            response.set_value("Conta deletado com sucesso")
            return True
        return False

    def update(self, id_form, account_form, response):
        new_account = model.AccountBusinessLogic.create_account_by_form(account_form)
        older_account = self.get_by_id(id_form, response)
        if older_account is None:
            response.set_value("Conta nao existe para ser atualizado")
        elif self.model.update(older_account, new_account):
            response.set_value("Conta atualizado com sucesso")
        else:
            response.set_value("Nao foi possivel atualizar")

    def get_by_id(self, id_form, response):
        response.set_value("Conta recuperado com sucesso")
        account = self.model.get_by_id(id_form.get_fields()['id'])
        if account is None:
            response.set_value("Conta nao existe")
        return account

    def get_all(self, response):
        response.set_value("Contas recuperados com sucesso")
        return self.model.get_all()

    def download(self):
        self.model.download()

    def upload(self):
        self.model.upload()
