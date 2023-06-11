import datetime
import model.Account
import model.Event


class Repository:

    def __init__(self, database):
        self.next_id = 0
        self.elements = []
        self.database = database

    def reset_elements(self):
        self.elements.clear()

    def reset_id(self):
        self.next_id = 0

    def add(self, element):
        element.set_id(self.next_id)
        self.elements.append(element)
        self.next_id += 1

    def delete_by_id(self, id):
        for element in self.elements:
            if element.get_id() == id:
                self.elements.remove(element)
                return True
        return False

    def update(self, older_element, new_element):
        if self.delete_by_id(older_element.id):
            self.add(new_element)
            return True
        return False

    def get_by_id(self, id):
        for element in self.elements:
            if element.get_id() == id:
                return element
        return None

    def get_all(self):
        return self.elements

    def upload(self):
        ...

    def download(self):
        ...


class EventRepository(Repository):

    def __init__(self, database):
        super().__init__(database)

    def get_by_date(self, date):
        events = []
        for event in self.get_all():
            if event.get_date() == date:
                events.append(event)
        return events

    def get_by_month(self, month):
        events = []
        current_time = datetime.datetime.now()
        for event in self.get_all():
            if event.get_date().get_month() == month and event.get_date().get_year() == current_time.year:
                events.append(event)
        return events

    def get_by_year(self, year):
        events = []
        for event in self.get_all():
            if event.get_date().get_year() == year:
                events.append(event)
        return events

    def download(self):
        self.reset_elements()
        events = self.database.download()
        events.remove('')
        events = events[1:]
        for event in events:
            event = event.split('|')

            date = event[0].split('/')
            period = event[1].split(' ')
            title = event[2]
            text = event[3]

            date = model.Event.Date(int(date[0]), int(date[1]), int(date[2]))
            if period[0] == "None":
                period = None
            else:
                period = model.Event.Period(int(period[0]), int(period[1]))
            description = model.Event.Description(title, text)
            self.add(model.Event.Event(date, period, description))

    def upload(self):
        events = self.get_all()
        lines = []
        for event in events:
            date = event.get_date()
            date = f"{date.get_day()}/{date.get_month()}/{date.get_year()}"
            period = event.get_period()
            if period is None:
                period = "None"
            else:
                period = f"{period.get_start_time()} {period.get_end_time()}"
            description = event.get_description()
            description = description.get_title() + "|" + description.get_text()
            line = (date + "|" + period + "|" + description)
            lines.append(line)
        self.database.upload(lines)


class AccountRepository(Repository):

    def __init__(self, database):
        super().__init__(database)

    def download(self):
        self.reset_elements()
        accounts = self.database.download()
        accounts.remove('')
        accounts = accounts[1:]
        for account in accounts:
            account = account.split('|')
            user = account[0]
            password = account[1]
            self.add(model.Account.Account(user, password))

    def upload(self):
        accounts = self.get_all()
        lines = []
        for account in accounts:
            line = account.get_user() + "|" + account.get_password()
            lines.append(line)
        self.database.upload(lines)
