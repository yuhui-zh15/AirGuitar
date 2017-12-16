var URL = 'http://0.0.0.0:5000';
var FETCH = '/fetch';

function fetch() {
    $.post(URL + FETCH, {'query': 'pick_string'},
    function(data, status) {
        if (data !== 'None')
            vibrateString(Number(data))
    });
}

setInterval(fetch, 50);
