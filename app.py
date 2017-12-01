import time
import Leap
from motion import AirListener, StrummingHandler, ChordHandler
from sound import Guitar, Player

class App(object):
    def start(self):
        print('AirGuitar Started')
        self.guitar = Guitar(Player())

        self.controller = Leap.Controller()
        self.controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)
        self.controller.config.set("Gesture.KeyTap.MinDownVelocity", 30.0)
        self.controller.config.set("Gesture.KeyTap.HistorySeconds", .2)
        self.controller.config.set("Gesture.KeyTap.MinDistance", 0.8)
        self.controller.config.save()
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
