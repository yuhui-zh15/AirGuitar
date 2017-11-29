from mingus.containers import Note, NoteContainer

class GuitarNote(Note):
    '''Represent a note on guitar.

    :param string: the number of the string,\
            from the thinnest(1) to the thickest(6)
    :type string: int
    :param fret: the fret(0-14)
    :tpye fret: int
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

class GuitarChord(NoteContainer):
    '''Return a list of notes in that chord

    :param chord_name: name of the chord
    :type chord_name: str

    .. code-block:: python

        from sound import Player, GuitarChord
        p = Player()
        G_chord = GuitarChord('G')
        p.play_notes(G_chord)
    '''
    chord_dict = {
        'G': [(1, 3), (2, 0), (3, 0), (4, 0), (5, 2), (6, 3)],
        'Am': [(1, 0), (2, 1), (3, 2), (4, 2), (5, 0)],
        'Bm': [(1, 2), (2, 3), (3, 4), (4, 4), (5, 2)],
        'C': [(1, 0), (2, 1), (3, 0), (4, 2), (5, 3)],
        'D': [(1, 2), (2, 3), (3, 2), (4, 0)],
        'Em': [(1, 0), (2, 0), (3, 0), (4, 2), (5, 2), (6, 0)],
        'Em7': [(1, 0), (2, 3), (3, 0), (4, 2), (5, 2), (6, 0)],
        'D7': [(1, 2), (2, 1), (3, 2), (4, 0)],
    }

    def __init__(self, chord_name):
        if chord_name not in self.chord_dict:
            print('Chord not added!')
            return
        chord_pos= self.chord_dict[chord_name]
        super(GuitarChord, self)\
            .__init__([GuitarNote(*pos) for pos in chord_pos])

