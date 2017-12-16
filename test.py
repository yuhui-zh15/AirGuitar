import eventlet
eventlet.monkey_patch()

import time
from threading import Thread
import Leap
from motion import AirListener, StrummingHandler, ChordHandler
from sound import Guitar, Player

guitar = Guitar(Player())
controller = Leap.Controller()
listener = AirListener()

listener.add_handler(ChordHandler(controller, guitar))
listener.add_handler(StrummingHandler(controller, guitar))

controller.add_listener(listener)

from flask import Flask, request
from flask_cors import CORS
from sound import fetch

app = Flask(__name__)
CORS(app)

@app.route("/fetch", methods=['POST'])
def picked():
    '''Use short polling to get buffered data.

    Method = post

    :params: query - 'pick_string'/'set_chord'
    '''
    if request.method == 'POST':
        query = request.form['query']
        fetched = fetch(query)
        if fetched is not None:
            print('Fetched', fetched)
        return str(fetched)

app.run(host='0.0.0.0', port=5000)
