var socket = io.connect('http://localhost:5000');

socket.on('connect', function() {
    socket.emit('my event', {data: 'I\'m connected!'});
    vibrateString(1);
});

$(document).ready(function() {

});
