import datetime
import model.EventBusinessLogic


class EventController:

    def __init__(self, _model):
        self.model = _model

    def add(self, event_form, response):
        event = model.EventBusinessLogic.create_event_by_form(event_form)
        if self.model.add(event):
            response.set_value("Evento adicionado com sucesso")
        else:
            response.set_value("Convergencia de eventos")

    def delete_by_id(self, id_form, response):
        id = model.EventBusinessLogic.create_id_by_form(id_form)
        response.set_value("Falha ao deletar")
        if self.model.delete_by_id(id):
            response.set_value("Evento deletado com sucesso")

    def update(self, id_form, event_form, response):
        new_event = model.EventBusinessLogic.create_event_by_form(event_form)
        id = model.EventBusinessLogic.create_id_by_form(id_form)
        older_event = self.model.get_by_id(id)
        if older_event is None:
            response.set_value("Evento nao existe para ser atualizado")
        elif self.model.update(older_event, new_event):
            response.set_value("Evento atualizado com sucesso")
        else:
            response.set_value("Nao foi possivel atualizar")

    def get_by_id(self, id_form, response):
        id = model.EventBusinessLogic.create_id_by_form(id_form)
        response.set_value("Evento recuperado com sucesso")
        event = self.model.get_by_id(id)
        if event is None:
            response.set_value("Evento nao existe")
        return event

    def get_by_date(self, date_form, response):
        date = model.EventBusinessLogic.create_date_by_form(date_form)
        response.set_value("Eventos recuperado com sucesso")
        return self.model.get_by_date(date)

    def get_by_month(self, month_form, response):
        month = model.EventBusinessLogic.create_month_by_form(month_form)
        response.set_value("Eventos recuperado com sucesso")
        return self.model.get_by_month(month)

    def get_by_year(self, year_form, response):
        year = model.EventBusinessLogic.create_year_by_form(year_form)
        response.set_value("Eventos recuperado com sucesso")
        return self.model.get_by_year(year)

    def get_all(self, response):
        response.set_value("Eventos recuperados com sucesso")
        return self.model.get_all()

    def get_statistic(self, response):
        response.set_value("Estatistica recuperada com sucesso")
        current_time = datetime.datetime.now()
        return self.model.get_by_year(current_time.year)

    def download(self):
        self.model.download()

    def upload(self):
        self.model.upload()
