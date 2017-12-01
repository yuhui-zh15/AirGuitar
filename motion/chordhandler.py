import Leap

class ChordHandler(object):
    '''Process a chord and use the data of left hand.

    :param controller: the Leap Controller instance.
    :param guitar: the guitar that the handler takes action on.
    '''

    chord_positions = [None, -150, -100, -50, 0, 50, 100]
    chord_list = [None, 'G', 'Am', 'Bm', 'C', 'D', 'Em']

    def __init__(self, controller, guitar):
        self.controller = controller
        self.guitar = guitar
        self.last_z = None
        print('Strumming handler added.')

    def process(self, frame):
        '''Capture the left hand's motion in the frame.'''
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

        new_z = index_finger.joint_position(Leap.Finger.JOINT_TIP).z
        self.move_to(new_z)

    def move_to(self, new_z):
        '''When the left index finger updates its position.

        Change chords when click.

        :param new_z: the new position on z axis
        :type new_z: float
        '''
        if (self.last_z == None):
            self.last_z = new_z
            return

        # Strumming down
        if self.last_z > new_z:
            for string in range(6, 0, -1):
                if self.last_z > self.chord_positions[string]\
                and self.chord_positions[string] > new_z:
                    self.guitar.set_chord(self.chord_list[string])

        # Strumming up
        if new_z > self.last_z:
            for string in range(1, 7):
                if self.last_z < self.chord_positions[string]\
                and self.chord_positions[string] < new_z:
                    self.guitar.set_chord(self.chord_list[string])

        self.last_z = new_z
