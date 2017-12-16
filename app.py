import time
import Leap
from motion import AirListener, StrummingHandler, ChordHandler
from sound import Guitar, Player, socket_player_start

class App(object):
    def start(self):
        print('AirGuitar Started')
        
        self.guitar = Guitar(Player())
        self.controller = Leap.Controller()
        self.listener = AirListener()

        self.listener.add_handler(ChordHandler(self.controller, self.guitar))
        self.listener.add_handler(StrummingHandler(self.controller, self.guitar))

        self.controller.add_listener(self.listener)

        socket_player_start()

class ConsoleApp(App):
    def start(self):
        super(ConsoleApp, self).start()

if __name__ == '__main__':
    app = ConsoleApp()
    app.start()
