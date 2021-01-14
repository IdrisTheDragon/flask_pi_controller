from flask import Flask, redirect, url_for, render_template, request, flash 
from flask_socketio import SocketIO, emit
from robot import robot_move, robot_speed


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    print('received message: ' + str(data))
    emit('message_response','{"data":"Hello, User"}', json=True)

@socketio.on('move')
def move(data):
    # print('received move: ' + str(data))
    robot_move.send(app,move_dir=data['move_dir'])

@socketio.on('speed')
def speed(data):
    # print('received move: ' + str(data))
    robot_speed.send(app,speed=data['speed'])

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')