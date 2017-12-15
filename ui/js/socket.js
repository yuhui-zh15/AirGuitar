var socket = io.connect('http://localhost:5000');

socket.on('connect', function() {
    socket.emit('on connect', {data: 'I\'m connected!'});
});

socket.on('pick', (stringId) => {
    vibrateString(stringId);
});

socket.on('set chord', (chordName) => {
    let idx = chordNames.indexOf(chordName);
    if (idx > -1)
    {
        selectChord(idx);
    }
    else
    {
        alert('Chord not added in chordNames[]');
    }
});
