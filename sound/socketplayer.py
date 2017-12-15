import eventlet
eventlet.monkey_patch()

from threading import Thread
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

def start_server():
    socketio.run(app)

thread = Thread(target=start_server)
def socket_player_start():
    thread.start()

def pick_string(string):
    socketio.emit('pick', string, broadcast=True)

def set_chord(chord_name):
    socketio.emit('set chord', chord_name, broadcast=True)

@socketio.on('on connect')
def handle_onConnect_event(json):
    print('received json: ' + str(json))
