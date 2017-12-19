var NUM_STRING = 6;
strings = new Array(NUM_STRING + 1);    // 1-indexed to keep consistent with python code.

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
 * Vibrates the ith guitar string when user swips the guitar with right hand.
 */
function vibrateString(i) {
    string = strings[i];
    var MAX_VIBRATE_COEFF = 8;

    // TODO: more elegant method required (could not get createjs to work...)
    var coeffExpand = 1;
    var intervalExpand = setInterval(function() {
        if (coeffExpand == MAX_VIBRATE_COEFF) {
            clearInterval(intervalExpand);
        } else {
            coeffExpand++;
            string.css('height', (2 + coeffExpand) + 'px');
            string.css('background-color', 'rgba(50, 50, 50, ' + (1.0 / (coeffExpand + 1)) + ')');
        }
    }, 50);

    var coeffShrink = MAX_VIBRATE_COEFF;
    var intervalShrink = setInterval(function() {
        if (coeffShrink == 0) {
            clearInterval(intervalShrink);
        } else {
            coeffShrink--;
            string.css('height', (2 + coeffShrink) + 'px');
            string.css('background-color', 'rgba(50, 50, 50, ' + (1.0 / (coeffShrink + 1)) + ')');
        }
    }, 50);
}

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
