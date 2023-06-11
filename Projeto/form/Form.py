import model.EventBusinessLogic
import model.AccountBusinessLogic


class Response:

    def __init__(self):
        self.value = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


class Field:

    def __init__(self, label):
        self.label = label
        self.value = ""

    def fill(self):
        print(f"{self.get_label():-^50}")
        print("Insira: ", end="")
        self.value = input()
        print("-" * 50)

    def get_label(self):
        return self.label

    def get_value(self):
        return self.value


class Form:

    def __init__(self):
        self.fields = {}

    def fill(self):
        ...

    def get_fields(self):
        return self.fields


class IdForm(Form):

    def __init__(self):
        super().__init__()
        self.fields['id'] = Field(" ID ")

    def fill(self):
        self.fields['id'].fill()


class MonthForm(Form):

    def __init__(self):
        super().__init__()
        self.fields['month'] = Field(" Mes ")

    def fill(self):
        self.fields['month'].fill()


class YearForm(Form):

    def __init__(self):
        super().__init__()
        self.fields['year'] = Field(" Ano ")

    def fill(self):
        self.fields['year'].fill()


class DateForm(Form):

    def __init__(self):
        super().__init__()
        self.fields['day'] = Field(" Dia ")
        self.fields['month'] = Field(" Mes ")
        self.fields['year'] = Field(" Ano ")

    def fill(self):
        print()
        print(f"{' Formulario data ':-^50}")
        self.fields['day'].fill()
        self.fields['month'].fill()
        self.fields['year'].fill()
        day = int(self.fields['day'].get_value())
        month = int(self.fields['month'].get_value())
        year = int(self.fields['year'].get_value())
        while not model.EventBusinessLogic.is_date_valid(day, month, year):
            print("Data inválida! Insira novamente")
            self.fields['day'].fill()
            self.fields['month'].fill()
            self.fields['year'].fill()
            day = int(self.fields['day'].get_value())
            month = int(self.fields['month'].get_value())
            year = int(self.fields['year'].get_value())
        print("-" * 50)
        print()


class PeriodForm(Form):

    def __init__(self):
        super().__init__()
        self.fields['start time'] = Field(" Inicio ")
        self.fields['end time'] = Field(" Fim ")

    def fill(self):
        print()
        print(f"{' Formulario periodo ':-^50}")
        print("Caso nao tenha periodo nao insira nada, apenas aperte enter")
        self.fields['start time'].fill()
        self.fields['end time'].fill()
        start_time = self.fields['start time'].get_value()
        end_time = self.fields['end time'].get_value()
        if len(start_time) < 1 or len(end_time) < 1:
            start_time = None
            end_time = None
        else:
            start_time = int(start_time)
            end_time = int(end_time)
        while not model.EventBusinessLogic.is_period_valid(start_time, end_time):
            print("Periodo inválido! Insira novamente")
            self.fields['start time'].fill()
            self.fields['end time'].fill()
            start_time = self.fields['start time'].get_value()
            end_time = self.fields['end time'].get_value()
            if len(start_time) < 1 or len(end_time) < 1:
                start_time = None
                end_time = None
            else:
                start_time = int(start_time)
                end_time = int(end_time)
        print("-" * 50)
        print()


class DescriptionForm(Form):

    def __init__(self):
        super().__init__()
        self.fields['title'] = Field(" Titulo ")
        self.fields['text'] = Field(" Texto ")

    def fill(self):
        print()
        print(f"{' Formulario descricao ':-^50}")
        self.fields['title'].fill()
        self.fields['text'].fill()
        print("-" * 50)
        print()


class EventForm(Form):

    def __init__(self):
        super().__init__()
        self.fields['date'] = DateForm()
        self.fields['period'] = PeriodForm()
        self.fields['description'] = DescriptionForm()

    def fill(self):
        print()
        print(f"{' Formulario evento ':-^50}")
        self.fields['date'].fill()
        self.fields['period'].fill()
        self.fields['description'].fill()
        print("-" * 50)
        print()


class AccountForm(Form):

    def __init__(self):
        super().__init__()
        self.fields['user'] = Field(" Usuario ")
        self.fields['password'] = Field(" Senha ")

    def fill(self):
        print()
        print(f"{' Formulario conta ':-^50}")
        self.fields['user'].fill()
        self.fields['password'].fill()
        while not model.AccountBusinessLogic.is_account_valid(self.fields['user'].get_value(),
                                                              self.fields['password'].get_value()):
            print("Conta inválida! Insira novamente")
            self.fields['user'].fill()
            self.fields['password'].fill()
        print("-" * 50)
        print()
