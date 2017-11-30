import Leap
from motion.swipehandler import SwipeHandler

class LeapEventListener(Leap.Listener):

    def __init__(self):
        super(LeapEventListener, self).__init__()
        self.handler_list = []

    def on_connect(self, controller):
        print("Connected")
        controller.set_policy(Leap.Controller.POLICY_BACKGROUND_FRAMES)

        # TODO: add left hand press chord handler
        # self.add_handler(PressHandler(controller))

        self.add_handler(SwipeHandler(controller))

    def on_disconnect(self, controller):
        print("Disconnected")

    def on_frame(self, controller):
        frame = controller.frame()
        for handler in self.handler_list:
            handler.process(frame)

    def add_handler(self, handler):
        self.handler_list.append(handler)
