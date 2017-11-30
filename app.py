import time
import Leap
from motion import LeapEventListener

class App(object):
    def start(self):
        print('AirGuitar Started')
        self.controller = Leap.Controller()
        self.listener = LeapEventListener()
        self.controller.add_listener(self.listener)

class ConsoleApp(App):
    def start(self):
        super(ConsoleApp, self).start()
        while True:
            time.sleep(1)

if __name__ == '__main__':
    app = ConsoleApp()
    app.start()
