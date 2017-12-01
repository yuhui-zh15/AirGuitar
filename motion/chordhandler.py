import Leap

class ChordHandler(object):
    '''Process a chord and use the data of left hand.

    :param controller: the Leap Controller instance.
    :param guitar: the guitar that the handler takes action on.
    '''

    division_x = [-200, -50]
    division_z = [-100, 100]

    chord_list = [['G', 'Am', 'Bm'], ['C', 'D', 'Em'], ['G', 'Am', 'Bm']] # Fron left to right, from up to bottom

    def __init__(self, controller, guitar):
        self.controller = controller
        self.guitar = guitar
        print('Chord handler added.')

    def process(self, frame):
        '''Capture the left hand's keytap in the frame.'''
        key_tap = None
        for gesture in frame.gestures():
            if gesture.type is Leap.Gesture.TYPE_KEY_TAP:
                key_tap = Leap.KeyTapGesture(gesture)
        if key_tap is None: return
        
        left_hand = None
        for hand in key_tap.hands:
            if hand.is_left:
                left_hand = hand
                break
        if left_hand is None: return

        touch_x, touch_z = key_tap.position.x, key_tap.position.z
        self.move_to(touch_x, touch_z)

    def move_to(self, touch_x, touch_z):
        '''When the left finger tap change chord.

        Change chords when keytap.

        :param touch_x: the new position on x axis
        :type touch_x: float
        :param touch_z: the new position on x axis
        :type touch_z: float
        '''

        if (touch_x < self.division_x[0]):
            x_index = 0
        elif (self.division_x[0] < touch_x and touch_x < self.division_x[1]):
            x_index = 1
        elif (self.division_x[1] < touch_x):
            x_index = 2

        if (touch_z < self.division_z[0]):
            z_index = 0
        elif (self.division_z[0] < touch_z and touch_z < self.division_z[1]):
            z_index = 1
        elif (self.division_z[1] < touch_z):
            z_index = 2
        
        # Set chord
        self.guitar.set_chord(self.chord_list[z_index][x_index])

