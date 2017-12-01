import time
import Leap
from motion import AirListener, StrummingHandler, ChordHandler
from sound import Guitar, Player

class App(object):
    def start(self):
        print('AirGuitar Started')
        self.guitar = Guitar(Player())
        self.controller = Leap.Controller()
        self.listener = AirListener()

        self.listener.add_handler(ChordHandler(self.controller, self.guitar))
        self.listener.add_handler(StrummingHandler(self.controller, self.guitar))

        self.controller.add_listener(self.listener)

class ConsoleApp(App):
    def start(self):
        super(ConsoleApp, self).start()
        while True:
            time.sleep(1)

if __name__ == '__main__':
    app = ConsoleApp()
    app.start()
