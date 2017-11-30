import Leap
from sound import Player, GuitarChord

class SwipeHandler(object):

    def __init__(self, controller):
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
        controller.config.set('Gesture.Swipe.MinLength', 200.0)
        controller.config.save()
        print('Swipe handler added.')

    def process(self, frame):
        swipe = None
        for gesture in frame.gestures():
            if gesture.type is Leap.Gesture.TYPE_SWIPE:
                swipe = Leap.SwipeGesture(gesture)

        if swipe is not None:
            if swipe.state == Leap.SwipeGesture.STATE_START\
            and Leap.Finger(swipe.pointable).type == Leap.Finger.TYPE_INDEX:
                print('Got swipe gesture! z=%f' % swipe.position.z)
                Player.play_notes(GuitarChord('random'))
