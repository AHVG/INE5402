import form.Form
import view.View
import view.Home
import database.Database
import model.Event
import model.Repository
import model.EventBusinessLogic
import controller.EventController


class Menu(view.View.View):

    def __init__(self, owner):
        super().__init__(owner)
        self.event_form = form.Form.EventForm()
        self.id_form = form.Form.IdForm()
        self.date_form = form.Form.DateForm()
        self.month_form = form.Form.MonthForm()
        self.year_form = form.Form.YearForm()
        self.response = form.Form.Response()

        event_database = database.Database.Database(f"events/{owner.get_user()}.txt",
                                                    ['DATE', 'PERIOD', 'TITLE', 'TEXT'])
        event_repository = model.Repository.EventRepository(event_database)
        event_business_logic = model.EventBusinessLogic.EventBusinessLogic(event_repository)
        event_controller = controller.EventController.EventController(event_business_logic)
        self.event_controller = event_controller

    def enter(self):
        self.event_controller.download()

    def leave(self):
        self.event_controller.upload()

    def show(self):
        print()
        print("-"*22 + " Menu " + "-"*22)
        print()
        print(f"{'1. Obter todos os eventos':^50}")
        print(f"{'2. Obter o evento por data':^50}")
        print(f"{'3. Obter o evento por mes':^50}")
        print(f"{'4. Obter o evento por ano':^50}")
        print(f"{'5. Obter o evento por id':^50}")
        print(f"{'6. Adicionar evento':^50}")
        print(f"{'7. Atualizar evento':^50}")
        print(f"{'8. Deletar evento':^50}")
        print(f"{'9. Estatistica':^50}")
        print(f"{'0. Home':^50}")
        print("-"*50)
        print()

    def get_all(self):
        print()
        print("-"*16 + " Todos os eventos " + "-"*16)
        events = self.event_controller.get_all(self.response)
        for event in events:
            model.Event.show_event(event)
        print(self.response.get_value())
        print("-"*50)
        print()

    def get_by_date(self):
        self.date_form.fill()
        print()
        print("-" * 12 + " Todos os eventos da data " + "-" * 12)
        events = self.event_controller.get_by_date(self.date_form, self.response)
        for event in events:
            model.Event.show_event(event)
        print(self.response.get_value())
        print("-"*50)
        print()

    def get_by_month(self):
        self.month_form.fill()
        print()
        print("-" * 12 + " Todos os eventos do mes " + "-" * 13)
        events = self.event_controller.get_by_month(self.month_form, self.response)
        for event in events:
            model.Event.show_event(event)
        print(self.response.get_value())
        print("-" * 50)
        print()

    def get_by_year(self):
        self.year_form.fill()
        print()
        print("-" * 12 + " Todos os eventos do ano " + "-" * 12)
        events = self.event_controller.get_by_year(self.year_form, self.response)
        for event in events:
            model.Event.show_event(event)
        print(self.response.get_value())
        print("-" * 50)
        print()

    def get_by_id(self):
        self.id_form.fill()
        print()
        print("-" * 16 + " Evento escolhido " + "-" * 16)
        event = self.event_controller.get_by_id(self.id_form, self.response)
        if event is not None:
            model.Event.show_event(event)
        print(self.response.get_value())
        print("-" * 50)
        print()

    def add(self):
        self.event_form.fill()
        self.event_controller.add(self.event_form, self.response)
        print(self.response.get_value())

    def update(self):
        self.get_all()

        print()
        print("Obs.: Para atualizar um evento, digite o ID dele e reescreva-o")
        print()
        self.id_form.fill()
        self.event_form.fill()
        self.event_controller.update(self.id_form, self.event_form, self.response)
        print(self.response.get_value())

    def delete_by_id(self):
        self.id_form.fill()
        self.event_controller.delete_by_id(self.id_form, self.response)
        print(self.response.get_value())

    def show_statistic(self):
        print()
        print("-" * 18 + " Estatistica do ANO " + "-" * 19)
        events = self.event_controller.get_statistic(self.response)
        for month in range(1, 13):
            number_of_events_per_month = 0
            for event in events:
                if event.get_date().get_month() == month:
                    number_of_events_per_month += 1
            print(f"{month:>2} - " + "#" * number_of_events_per_month)
        print()
        print(f"Media por mes - {float(len(events)/12):.2}")
        print()
        print(self.response.get_value())
        print("-" * 50)
        print()

    def run(self):
        while True:
            self.show()
            print("Insira a requesicao: ", end="")
            request = int(input())
            if request == 0:
                self.owner.set_next_screen(view.Home.Home(self.owner))
                break
            elif request == 1:
                self.get_all()
            elif request == 2:
                self.get_by_date()
            elif request == 3:
                self.get_by_month()
            elif request == 4:
                self.get_by_year()
            elif request == 5:
                self.get_by_id()
            elif request == 6:
                self.add()
            elif request == 7:
                self.update()
            elif request == 8:
                self.delete_by_id()
            elif request == 9:
                self.show_statistic()
            else:
                print("Nao entendi!")
