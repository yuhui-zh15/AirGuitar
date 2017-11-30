import Leap

class SwipeHandler(object):

    def __init__(self, controller):
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
        controller.config.set('Gesture.Swipe.MinLength', 200.0)
        controller.config.save()
        print('Swipe handler added.')

    def process(self, frame):
        print('Swipe handler doing frame.')
