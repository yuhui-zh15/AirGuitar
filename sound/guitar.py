from mingus.containers import Note

class GuitarNote(Note):
    '''Represent a note on guitar.

    :param string: the number of the string,\
            from the thinnest(1) to the thickest(6)
    :type string: int
    :param fret: the fret(0-14)
    :type fret: int
    '''

    open_string_notes = {
        1: 52, #'E-4'
        2: 47, #'B-3'
        3: 43, #'G-3'
        4: 38, #'D-3'
        5: 33, #'A-2'
        6: 28, #'E-2'
    }

    def __init__(self, string, fret):
        super(GuitarNote, self)\
            .__init__(self.open_string_notes[string] + fret)

class Guitar(object):
    '''A guitar simulator.

    :param player: a Player instance which should have `play_notes()` method.
    '''

    chord_dict = {
        'G': [(1, 3), (2, 0), (3, 0), (4, 0), (5, 2), (6, 3)],
        'Am': [(1, 0), (2, 1), (3, 2), (4, 2), (5, 0)],
        'Bm': [(1, 2), (2, 3), (3, 4), (4, 4), (5, 2)],
        'C': [(1, 0), (2, 1), (3, 0), (4, 2), (5, 3)],
        'D': [(1, 2), (2, 3), (3, 2), (4, 0)],
        'F': [(1, 1), (2, 1), (3, 2), (4, 3), (5, 1), (6, 1)],
        'Dm': [(1, 1), (2, 3), (3, 2), (4, 0)],
        'Em': [(1, 0), (2, 0), (3, 0), (4, 2), (5, 2), (6, 0)],
        'Em7': [(1, 0), (2, 3), (3, 0), (4, 2), (5, 2), (6, 0)],
        'D7': [(1, 2), (2, 1), (3, 2), (4, 0)],
    }

    def __init__(self, player):
        self.reset()
        self.player = player

    def reset(self):
        '''Release the left hand.'''
        self.string_states = [0] * 7

    def set_string(self, string, fret):
        '''Press down a fret on a string.

        :param string: the number of the string (1~6)
        :type string: int
        :param fret: the number of the fret (-1~14). -1 for mute. 0 for open.
        :type fret: int
        '''
        if 1 <= string and string <= 6 and -1 <= fret and fret <= 14:
            self.string_states[string] = fret
            print('Set string %d fret %d' % (string, fret))
        else:
            print('String or fret index out of range!')

    def set_chord(self, chord_name):
        '''Press a chord on the guitar.

        Note: all previously set states will be discarded.

        :param chord_name: name of the chord
        :type chord_name: str
        '''
        if chord_name not in self.chord_dict:
            print('Chord not added!')
            return
        # Mute all the strings
        self.string_states = [-1] * 7
        # Get pressed positions
        chord_pos = self.chord_dict[chord_name]
        for pos in chord_pos:
            self.set_string(*pos)

        self.player.set_chord(chord_name)
        print('Set chord ' + chord_name)

    def play_string(self, string):
        '''Play a specific string'''
        if 1 <= string and string <= 6:
            if self.string_states[string] >= 0:
                self.player.pick_string(string)
                self.player.play_notes(GuitarNote(string, self.string_states[string]))
        else:
            print('String index out of range!')
