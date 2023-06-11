import view.View
import view.Home


class Application:

    def __init__(self):
        self.current_screen = view.Home.Home(self)
        self.next_screen = None
        self.running = True
        self.user = ""

    def get_user(self):
        return self.user

    def set_user(self, user):
        self.user = user

    def close(self):
        self.running = False

    def is_running(self):
        return self.running

    def set_next_screen(self, next_screen):
        self.next_screen = next_screen

    def change_screen(self):
        self.current_screen.leave()
        self.current_screen = self.next_screen
        self.current_screen.enter()

    def run(self):
        self.current_screen.enter()
        while self.is_running():
            self.current_screen.run()
            self.change_screen()
