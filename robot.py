from flask.signals import Namespace

namespace = Namespace()
robot_move = namespace.signal('robot_move')
robot_speed = namespace.signal('robot_speed')

@robot_move.connect
def move(app, move_dir):
    if move_dir == 1:
        print('foreward')
    elif move_dir == 2:
        print('right')
    elif move_dir == 3:
        print('back')
    elif move_dir == 4:
        print('left')
    elif move_dir == 5:
        print('stop')

@robot_speed.connect
def speed(app, speed):
    if speed == 0:
        print('speed up')
    elif speed == 1:
        print('speed down')