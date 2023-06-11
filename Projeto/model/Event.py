import model.Element


# Classe para armazenar a data do evento
class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def set_day(self, day):
        self.day = day

    def get_day(self):
        return self.day

    def set_month(self, month):
        self.month = month

    def get_month(self):
        return self.month

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def __eq__(self, other):
        if (self.get_day() == other.get_day() and
            self.get_month() == other.get_month() and
                self.get_year() == other.get_year()):
            return True
        return False


# Classe para armazenar o periodo em que ocorre um evento do tipo tarefa presencial (FaceToFaceTask)
class Period:

    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def set_start_time(self, start_time):
        self.start_time = start_time

    def get_start_time(self):
        return self.start_time

    def set_end_time(self, end_time):
        self.end_time = end_time

    def get_end_time(self):
        return self.end_time


# Classe para armazenar uma descrição para o evento
class Description:

    def __init__(self, title, text):
        self.title = title
        self.text = text

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_text(self, text):
        self.text = text

    def get_text(self):
        return self.text


# Classe que representa um evento
class Event(model.Element.Element):

    def __init__(self, date, period, description):
        super().__init__()
        self.date = date
        self.period = period
        self.description = description

    def set_date(self, date):
        self.date = date

    def get_date(self):
        return self.date

    def set_period(self, period):
        self.period = period

    def get_period(self):
        return self.period

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description


def show_event(event):
    id = event.get_id()
    date = event.get_date()
    period = event.get_period()
    if period is None:
        period = "Nao tem periodo"
    else:
        period = "Das " + str(period.get_start_time()) + " ate " + str(period.get_end_time())
    description = event.get_description()
    print()
    print(f"{'Evento':^50}")
    print(f"{f'ID: {id}':^50}")
    print(f"{f'Data: {date.get_day()}/{date.get_month()}/{date.get_year()}':^50}")
    print(f"{f'Periodo: {period}':^50}")
    print(f"{f'Titulo: {description.get_title()}':^50}")
    print(f"{f'Texto: {description.get_text()}':^50}")
    print()
