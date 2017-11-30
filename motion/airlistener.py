import Leap

class AirListener(Leap.Listener):

    def __init__(self):
        super(AirListener, self).__init__()
        self.handler_list = []

    def on_connect(self, controller):
        print("Connected")
        controller.set_policy(Leap.Controller.POLICY_BACKGROUND_FRAMES)

    def on_disconnect(self, controller):
        print("Disconnected")

    def on_frame(self, controller):
        frame = controller.frame()
        for handler in self.handler_list:
            handler.process(frame)

    def add_handler(self, handler):
        self.handler_list.append(handler)
