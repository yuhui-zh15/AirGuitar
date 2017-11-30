from mingus.containers import Note, NoteContainer
from mingus.midi import fluidsynth

class Player:
    '''Use this to play notes.

    :param live: if the notes should be played immediately when added.
    :type live: bool
    '''

    fluidsynth.init('raw/FluidR3_GM.sf2')
    fluidsynth.set_instrument(1, 25)

    live = True

    @staticmethod
    def play_notes(notes):
        '''Add a note or a list of notes to the player
        :param notes: can be a note(int/str/Note) or \
                notes(list of int, NoteContainer)

        .. code-block:: python

            from sound import Player, GuitarNote
            Player.play_notes(48)                # play C-4
            Player.play_notes('C-4')             # play C-4
            Player.play_notes(GuitarNote(1, 1))  # play fret 1 on string 1
            G_chord = [GuitarNote(1, 3), GuitarNote(2, 0), GuitarNote(3, 0),\
                    GuitarNote(4, 0), GuitarNote(5, 2), GuitarNote(6, 3)]
            Player.play_notes(G_chord)
        '''
        try:
            notes = Note(notes)
        except Exception:
            pass
        try:
            notes = NoteContainer([Note(note) for note in notes])
        except Exception:
            pass

        if Player.live is True:
            if isinstance(notes, Note):
                fluidsynth.play_Note(notes)
                print('Playing Note', notes)
            if isinstance(notes, NoteContainer):
                fluidsynth.play_NoteContainer(notes)
                print('Playing Notes', notes)
        else:
            # TODO: keep the notes in a event list.
            pass
