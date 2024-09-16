from flask import Flask, send_from_directory, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__, static_folder='.')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode='eventlet')

@app.route('/')
def chat():
    return render_template('.', 'chat.html')


@app.route('/')
def serve_static():
    return send_from_directory('.', 'chat.css')
@app.route('/')
def serve_statics():
    return send_from_directory('.', 'chat.js')

@socketio.on('send_message')
def handle_message(message):
    emit('receive_message', message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, port=2710, debug=True)
