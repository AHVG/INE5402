import view.View
import view.Registration
import view.Login


class Home(view.View.View):

    def __init__(self, owner):
        super().__init__(owner)

    def show(self):
        print()
        print("-"*22 + " Home " + "-"*22)
        print()
        print(f"{'1. Entrar':^50}")
        print(f"{'2. Cadastrar':^50}")
        print(f"{'0. Sair':^50}")
        print("-"*50)
        print()

    def run(self):
        while True:
            self.show()
            print("Insira a requesicao: ", end="")
            request = int(input())
            if request == 1:
                self.owner.set_next_screen(view.Login.Login(self.owner))
                break
            elif request == 2:
                self.owner.set_next_screen(view.Registration.Registration(self.owner))
                break
            elif request == 0:
                self.owner.close()
                break
            else:
                print("Nao entendi!")
