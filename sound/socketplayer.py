import eventlet
eventlet.monkey_patch()

from threading import Thread
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

def start_server():
    socketio.run(app)

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

thread = Thread(target=start_server)
if __name__ == '__main__':
    thread.start()
    while True:
        socketio.sleep(1)
        socketio.emit('strum', 1, broadcast=True)
