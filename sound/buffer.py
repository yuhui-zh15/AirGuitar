strings_picked = []
chords_set= []
to_send_string = 0
to_send_chord= 0
track_chord_name = 'Em'

def fetch(query):
    if query == 'pick_string':
        global strings_picked, to_send_string
        if to_send_string < len(strings_picked):
            to_send_string += 1
            return strings_picked[to_send_string - 1]

    if query == 'track_chord':
        return track_chord_name

    if query == 'set_chord':
        global chords_set, to_send_chord
        if to_send_chord < len(chords_set):
            to_send_chord += 1
            return chords_set[to_send_chord - 1]

def pick_string(string):
    print('pick_string', string)
    strings_picked.append(string)

def set_chord(chord_name):
    print('set_chord', chord_name)
    chords_set.append(chord_name)
