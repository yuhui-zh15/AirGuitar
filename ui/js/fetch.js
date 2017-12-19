var URL = 'http://0.0.0.0:5000';
var FETCH = '/fetch';

function fetch() {
    $.post(URL + FETCH, {'query': 'pick_string'},
    function(data, status) {
        if (data !== 'None')
        {
            vibrateString(Number(data))
        }
    });

    $.post(URL + FETCH, {'query': 'set_chord'},
    function(data, status) {
        if (data !== 'None')
        {
            let chord_idx = chordNames.indexOf(data);
            if (chord_idx > -1)
            {
                selectChord(chord_idx);
            }
        }
    });
}

setInterval(fetch, 50);
