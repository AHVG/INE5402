
class View:

    def __init__(self, owner):
        self.owner = owner

    def enter(self):
        ...

    def leave(self):
        ...

    def show(self):
        ...

    def run(self):
        ...
