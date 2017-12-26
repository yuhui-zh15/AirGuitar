import Leap
import sound.buffer

class ChordHandler(object):
    '''Process a chord and use the data of left hand.

    :param controller: the Leap Controller instance.
    :param guitar: the guitar that the handler takes action on.
    '''

    division_x = [-80, -30]
    division_z = [-25, 25]

    chord_list = [['Em', 'Am', 'Dm'], ['G', 'C', 'F'], ['Em7', 'D', 'Bm']] # Fron left to right, from up to bottom

    def __init__(self, controller, guitar):
        self.controller = controller
        self.guitar = guitar
        print('Chord handler added.')

    def process(self, frame):
        '''Capture the left hand's keytap in the frame.'''
        left_hand = None
        for hand in frame.hands:
            if hand.is_left:
                left_hand = hand
                break
        if left_hand is None: return

        index_finger = None
        for finger in left_hand.fingers:
            if finger.type == Leap.Finger.TYPE_INDEX:
                index_finger = finger
                break
        if index_finger is None: return

        touch_x = index_finger.joint_position(Leap.Finger.JOINT_TIP).x
        touch_z = index_finger.joint_position(Leap.Finger.JOINT_TIP).z

        self.move_to(touch_x, touch_z)

        touch_y = index_finger.joint_position(Leap.Finger.JOINT_TIP).y
        if touch_y < 80:
            self.guitar.set_chord(sound.buffer.track_chord_name)

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
        sound.buffer.track_chord_name = self.chord_list[z_index][x_index]
