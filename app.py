import Leap
from motion import AirListener, StrummingHandler, ChordHandler
from sound import Guitar, Player, fetch

from flask import Flask, request
from flask_cors import CORS
import logging
app = Flask(__name__)
CORS(app)
logger = logging.getLogger('werkzeug')
logger.setLevel(logging.ERROR)

@app.route("/fetch", methods=['POST'])
def picked():
    '''Use short polling to get buffered data.

    Method = post

    :params: query - 'pick_string'/'set_chord'
    '''
    query = request.form['query']
    fetched = fetch(query)
    if fetched is not None:
        print('Fetched', fetched)
    return str(fetched)

class App(object):
    def start(self):
        print('AirGuitar Started')

        self.guitar = Guitar(Player())
        self.controller = Leap.Controller()
        self.listener = AirListener()

        self.listener.add_handler(ChordHandler(self.controller, self.guitar))
        self.listener.add_handler(StrummingHandler(self.controller, self.guitar))

        self.controller.add_listener(self.listener)

        app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    App().start()
