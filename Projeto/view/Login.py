import view.View
import view.Menu
import view.Home
import database.Database
import model.Account
import model.Repository
import model.AccountBusinessLogic
import controller.AccountController
import form.Form


class Login(view.View.View):

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

    def show(self):
        print()
        print("-"*20 + " Login " + "-"*20)
        print()
        print(f"{'Aqui voce faz seu login!':^50}")
        print()
        print("-"*50)
        print()

    def validation(self):
        self.account_form.fill()
        response = form.Form.Response()
        if self.account_controller.account_exist(self.account_form, response):
            self.owner.set_user(response.get_value())
            self.owner.set_next_screen(view.Menu.Menu(self.owner))
        else:
            self.owner.set_next_screen(view.Home.Home(self.owner))
            print(response.get_value())

    def run(self):
        self.show()
        self.validation()
