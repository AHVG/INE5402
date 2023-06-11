
class Database:

    def __init__(self, name, columns):
        self.name = name
        self.columns = columns
        self.initialize()

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_columns(self):
        return self.columns

    def initialize(self):
        with open(self.get_name(), "a") as _:
            with open(self.get_name(), "r") as file:
                if len(file.read()) < 1:
                    with open(self.get_name(), "a") as __:
                        first_line = ""
                        for column in self.get_columns():
                            first_line += column + "|"
                        first_line = first_line[:len(first_line) - 1]
                        self.write(first_line)

    def write(self, text):
        with open(self.get_name(), "a") as file:
            file.write(text + "\n")

    def download(self):
        with open(self.get_name(), 'r') as file:
            content = file.read()
        return content.split("\n")

    def upload(self, content):
        with open(self.get_name(), 'w'):
            ...
        self.initialize()
        for line in content:
            self.write(line)
