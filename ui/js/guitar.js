var NUM_STRING = 6;
strings = new Array(NUM_STRING + 1);    // 1-indexed to keep consistent with python code.
steps = new Array(NUM_STRING + 1);

var NUM_CHORD = 9;
chordNames = ['G', 'Am', 'Bm', 'C', 'D', 'Em', 'G', 'Am', 'Bm'];
chordSelects = new Array(NUM_CHORD);    // 0-indexed to keep consistent with python code.
currentChord = null;

$(document).ready(function() {
    for (var i = 1; i <= NUM_STRING; i++) {
        createString(i);
    }

    for (var i = 0; i < NUM_CHORD; i++) {
        createChordSelect(i);
    }

    // Currently the positions are hard-coded, but by using 'vh' & 'vw',
    // they are supposed to be constrained by a percentage w.r.t the viewport.
    function createString(i) {
        var START_TOP = 60;
        var SPACING = 5;
        var THICKNESS = 1 + i / 2; 
        string = jQuery('<hr/>', {
            id: 'string' + i,
            class: 'guitar-string'
        });
        $('#container-right').append(string);
        string.css('height', THICKNESS + 'px');
        string.css('top', (START_TOP + i * SPACING) + 'vh');
        strings[i] = string;
        steps[i] = 16;
    }

    function createChordSelect(i) {
        var START_TOP = 25;
        var START_LEFT = 33;
        var sideLen = Math.sqrt(NUM_CHORD);
        var sizeH = 12 * 1.2;
        var sizeW = 7.5 * 1.2;
        chordSelect = jQuery('<div/>', {
            id: 'chord' + i,
            class: 'chord-select',
            text: chordNames[i]
        });
        chordSelect.click(function() {
            selectChord(i);
        })
        $('#container-bottom').append(chordSelect);
        chordSelect.css('height', sizeH + 'vh');
        chordSelect.css('width', sizeW + 'vw');
        chordSelect.css('top', ((START_TOP + Math.floor(i / sideLen) * (sizeH * 1.15)) + 'vh'));
        chordSelect.css('left', ((START_LEFT + (i % sideLen) * (sizeW * 1.15)) + 'vw'));
        chordSelects[i] = chordSelect;
    }
});

/**
 * Actions to take when user sets a chord with left hand.
 */
function selectChord(i) {
    chordSelects[i].css('background-color', 'rgba(50, 20, 0, 0.3)');
    if (currentChord != null && currentChord != chordSelects[i]) {
        currentChord.css('background-color', 'rgba(50, 50, 50, 0.3)');
    }
    currentChord = chordSelects[i];
}


/**
 * Vibrates the ith guitar string when user swips the guitar with right hand.
 */
function vibrateString(i) {
    if (steps[i] > 8) {
        steps[i] = 16 - steps[i];
    }
}

function updateStrings() {
    heights = [3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3];
    colors = [
        'rgba(50, 50, 50, 0.5)',
        'rgba(50, 50, 50, 0.333333333333)',
        'rgba(50, 50, 50, 0.25)',
        'rgba(50, 50, 50, 0.2)',
        'rgba(50, 50, 50, 0.166666666667)',
        'rgba(50, 50, 50, 0.142857142857)',
        'rgba(50, 50, 50, 0.125)',
        'rgba(50, 50, 50, 0.111111111111)',
        'rgba(50, 50, 50, 0.111111111111)',
        'rgba(50, 50, 50, 0.125)',
        'rgba(50, 50, 50, 0.142857142857)',
        'rgba(50, 50, 50, 0.166666666667)',
        'rgba(50, 50, 50, 0.2)',
        'rgba(50, 50, 50, 0.25)',
        'rgba(50, 50, 50, 0.333333333333)',
        'rgba(50, 50, 50, 0.5)'
    ];
    for (var i = 1; i <= NUM_STRING; i++) {
        if (steps[i] != 16) {
            strings[i].css('height', (heights[steps[i]] - 2 + i / 2) + 'px');
            strings[i].css('background-color', colors[steps[i]]);
            steps[i]++;
        }
    }
}

setInterval(updateStrings, 30);