var NUM_STRING = 6;
strings = new Array(NUM_STRING + 1);    // 1-indexed to keep consistent with python code.
steps = new Array(NUM_STRING + 1);

var NUM_CHORD = 9;
chordNames = ['Em', 'Am', 'Dm', 'G', 'C', 'F', 'Em7', 'D', 'Bm'];
chordSelects = new Array(NUM_CHORD);    // 0-indexed to keep consistent with python code.
currentChord = null;
selectedChord = null;

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
        var START_TOP = 36.8;
        var SPACING = 3.55;
        var THICKNESS = 9.8;
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
        var START_TOP = 1;
        var START_LEFT = 1;
        var sideLen = Math.sqrt(NUM_CHORD);
        var sizeH = 12 * 0.8;
        var sizeW = 7.5 * 0.8;
        chordSelect = jQuery('<div/>', {
            id: 'chord' + i,
            class: 'chord-select',
            text: chordNames[i]
        });
        $('#container-bottom').append(chordSelect);
        chordSelect.css('height', sizeH + 'vh');
        chordSelect.css('width', sizeW + 'vw');
        chordSelect.css('top', ((START_TOP + Math.floor(i / sideLen) * (sizeH * 1.15)) + 'vh'));
        chordSelect.css('left', ((START_LEFT + (i % sideLen) * (sizeW * 1.15)) + 'vw'));
        chordSelects[i] = chordSelect;
    }
});

/**
 * Actions to take when the user moves left hand.
 */
function trackChord(i) {
    console.log('track' + chordSelects[i]);
    if (chordSelects[i] !== selectedChord)
    {
        chordSelects[i].css('background-color', 'rgba(50, 20, 0, 0.3)');
    }
    if (currentChord !== null && currentChord !== chordSelects[i] &&
        currentChord !== selectedChord) {
        currentChord.css('background-color', 'rgba(255, 255, 255, 0.3)');
    }
    currentChord = chordSelects[i];
}

/**
 * Actions to take when the user tap and select a chord.
 */
function selectChord(i) {
    console.log('select' + chordSelects[i]);
    chordSelects[i].css('background-color', 'rgba(50, 100, 50, 0.3)');
    if (selectedChord != null && selectedChord != chordSelects[i]) {
        selectedChord.css('background-color', 'rgba(255, 255, 255, 0.3)');
    }
    selectedChord = chordSelects[i];
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
        'rgba(255, 255, 255, 1)',
        'rgba(255, 255, 255, 0.5)',
        'rgba(255, 255, 255, 0.333)',
        'rgba(255, 255, 255, 0.2)',
        'rgba(255, 255, 255, 0.166666666667)',
        'rgba(255, 255, 255, 0.142857142857)',
        'rgba(255, 255, 255, 0.125)',
        'rgba(255, 255, 255, 0.111111111111)',
        'rgba(255, 255, 255, 0.111111111111)',
        'rgba(255, 255, 255, 0.125)',
        'rgba(255, 255, 255, 0.142857142857)',
        'rgba(255, 255, 255, 0.166666666667)',
        'rgba(255, 255, 255, 0.2)',
        'rgba(255, 255, 255, 0.333)',
        'rgba(255, 255, 255, 0.5)',
        'rgba(255, 255, 255, 1)'
    ];
    for (var i = 1; i <= NUM_STRING; i++) {
        if (steps[i] != 16) {
            strings[i].css('height', (heights[steps[i]] * 3 - 2 + i / 2) + 'px');
            strings[i].css('background-color', colors[steps[i]]);
            steps[i]++;
        }
    }
}

setInterval(updateStrings, 30);
