import view.View
import view.Home
import form.Form
import database.Database
import model.Repository
import model.AccountBusinessLogic
import controller.AccountController
import form.Form


class Registration(view.View.View):

    def __init__(self, owner):
        super().__init__(owner)
        account_database = database.Database.Database("accounts/accounts.txt", ['USER', 'PASSWORD'])
        account_repository = model.Repository.AccountRepository(account_database)
        account_business_logic = model.AccountBusinessLogic.AccountBusinessLogic(account_repository)
        account_controller = controller.AccountController.AccountController(account_business_logic)
        self.account_controller = account_controller
        self.account_form = form.Form.AccountForm()

    def enter(self):
        self.account_controller.download()

    def leave(self):
        self.account_controller.upload()

    def show(self):
        print()
        print("-"*20 + " Cadastro " + "-"*20)
        print()
        print(f"{'Aqui voce faz seu cadastro!':^50}")
        print()
        print("-"*50)
        print()

    def add_account(self):
        self.account_form.fill()
        response = form.Form.Response()
        self.account_controller.add(self.account_form, response)
        print(response.get_value())

    def run(self):
        self.show()
        self.add_account()
        self.owner.set_next_screen(view.Home.Home(self.owner))
