import model.Event


def create_id_by_form(id_form):
    field = id_form.get_fields()['id']
    return int(field.get_value())


def create_month_by_form(month_form):
    field = month_form.get_fields()['month']
    return int(field.get_value())


def create_year_by_form(year_form):
    field = year_form.get_fields()['year']
    return int(field.get_value())


def create_date_by_form(date_form):
    fields = date_form.get_fields()
    return model.Event.Date(int(fields['day'].get_value()),
                            int(fields['month'].get_value()),
                            int(fields['year'].get_value()))


def create_period_by_form(period_form):
    fields = period_form.get_fields()
    if fields['start time'] is None or fields['end time'] is None:
        return None
    return model.Event.Period(int(fields['start time'].get_value()),
                              int(fields['end time'].get_value()))


def create_description_by_form(description_form):
    fields = description_form.get_fields()
    return model.Event.Description(fields['title'].get_value(), fields['text'].get_value())


def create_event_by_form(event_form):
    forms = event_form.get_fields()
    date = create_date_by_form(forms['date'])
    period = create_period_by_form(forms['period'])
    description = create_description_by_form(forms['description'])
    return model.Event.Event(date, period, description)


def overlap(event_1, event_2):
    date_1 = event_1.get_date()
    date_2 = event_2.get_date()
    period_1 = event_1.get_period()
    period_2 = event_2.get_period()
    if period_1 is None or period_2 is None:
        return False
    elif date_1 != date_2:
        return False
    elif (period_1.get_end_time() <= period_2.get_start_time() or
            period_2.get_end_time() <= period_1.get_start_time()):
        return False
    return True


def is_date_valid(day, month, year):

    valid = False
    # Meses com 31 dias
    if (month == 1 or month == 3 or month == 5 or month == 7 or
            month == 8 or month == 10 or month == 12):
        if 0 < day <= 31:
            valid = True
    # Meses com 30 dias
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day <= 30:
            valid = True
    elif month == 2:
        # Testa se é bissexto
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if day <= 29:
                valid = True
        elif day <= 28:
            valid = True

    return valid


def is_period_valid(start_time, end_time):
    if start_time is None or end_time is None:
        return True
    if -1 < start_time < 24 and -1 < end_time < 24 and start_time < end_time:
        return True
    return False


class EventBusinessLogic:

    def __init__(self, repository):
        self.repository = repository

    def add(self, event):
        events = self.get_all()
        for other in events:
            if overlap(event, other):
                return False
        self.repository.add(event)
        return True

    def delete_by_id(self, id):
        return self.repository.delete_by_id(id)

    def update(self, older_event, new_event):
        return self.repository.update(older_event, new_event)

    def get_by_id(self, id):
        return self.repository.get_by_id(id)

    def get_all(self):
        return self.repository.get_all()

    def get_by_date(self, date):
        return self.repository.get_by_date(date)

    def get_by_month(self, month):
        return self.repository.get_by_month(month)

    def get_by_year(self, year):
        return self.repository.get_by_year(year)

    def download(self):
        self.repository.download()

    def upload(self):
        self.repository.upload()
