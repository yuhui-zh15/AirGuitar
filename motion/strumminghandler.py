import Leap

class StrummingHandler(object):
    '''Process a frame and use the data of right hand.

    :param controller: the Leap Controller instance.
    :param guitar: the guitar that the handler takes action on.
    '''

    string_positions = [None, -150, -100, -50, 0, 50, 100]

    def __init__(self, controller, guitar):
        self.controller = controller
        self.guitar = guitar
        self.last_z = None
        self.max_y = 220 # play NO sound when index finger is too high
        print('Strumming handler added.')

    def process(self, frame):
        '''Capture the right hand's motion in the frame.'''
        right_hand = None
        for hand in frame.hands:
            if hand.is_right:
                right_hand = hand
                break
        if right_hand is None: return

        index_finger = None
        for finger in right_hand.fingers:
            if finger.type == Leap.Finger.TYPE_INDEX:
                index_finger = finger
                break
        if index_finger is None: return

        new_y = index_finger.joint_position(Leap.Finger.JOINT_TIP).y
        if new_y > self.max_y: return

        new_z = index_finger.joint_position(Leap.Finger.JOINT_TIP).z
        self.move_to(new_z)

    def move_to(self, new_z):
        '''When the right index finger updates its position.

        Play notes when it passes a string.

        :param new_z: the new position on z axis
        :type new_z: float
        '''
        if (self.last_z == None):
            self.last_z = new_z
            return

        # Strumming down
        if self.last_z > new_z:
            for string in range(6, 0, -1):
                if self.last_z > self.string_positions[string]\
                and self.string_positions[string] > new_z:
                    self.guitar.play_string(string)

        # Strumming up
        if new_z > self.last_z:
            for string in range(1, 7):
                if self.last_z < self.string_positions[string]\
                and self.string_positions[string] < new_z:
                    self.guitar.play_string(string)

        self.last_z = new_z
