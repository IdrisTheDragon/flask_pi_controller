from flask.signals import Namespace

import RPi.GPIO as GPIO

L1 = 14
L2 = 15
Len = 18

R1 = 23
R2 = 24
Ren = 25

namespace = Namespace()
robot_move = namespace.signal('robot_move')
robot_speed = namespace.signal('robot_speed')

def setupGPIO():
    # mode 
    GPIO.setmode(GPIO.BCM)

    #L motor
    GPIO.setup(L1,GPIO.OUT)
    GPIO.output(L1,GPIO.LOW)
    GPIO.setup(L2,GPIO.OUT)
    GPIO.output(L2,GPIO.LOW)
    GPIO.setup(Len,GPIO.OUT)
    Lpwm = GPIO.PWM(Len,1000)
    Lpwm.start(25)

    # R motor
    GPIO.setup(R1,GPIO.OUT)
    GPIO.output(R1,GPIO.LOW)
    GPIO.setup(R2,GPIO.OUT)
    GPIO.output(R2,GPIO.LOW)
    GPIO.setup(Ren,GPIO.OUT)
    Rpwm = GPIO.PWM(Ren,1000)
    Rpwm.start(25)

@robot_move.connect
def move(app, move_dir):
    if move_dir == 1:
        print('foreward')
        GPIO.output(R1,GPIO.HIGH)
        GPIO.output(R2,GPIO.LOW)
        GPIO.output(L1,GPIO.HIGH)
        GPIO.output(L2,GPIO.LOW)
    elif move_dir == 2:
        print('right')
        GPIO.output(R1,GPIO.HIGH)
        GPIO.output(R2,GPIO.LOW)
        GPIO.output(L1,GPIO.LOW)
        GPIO.output(L2,GPIO.HIGH)
    elif move_dir == 3:
        print('back')
        GPIO.output(R1,GPIO.LOW)
        GPIO.output(R2,GPIO.HIGH)
        GPIO.output(L1,GPIO.LOW)
        GPIO.output(L2,GPIO.HIGH)
    elif move_dir == 4:
        print('left')
        GPIO.output(R1,GPIO.LOW)
        GPIO.output(R2,GPIO.HIGH)
        GPIO.output(L1,GPIO.HIGH)
        GPIO.output(L2,GPIO.LOW)
    elif move_dir == 5:
        print('stop')
        GPIO.output(R1,GPIO.LOW)
        GPIO.output(R2,GPIO.LOW)
        GPIO.output(L1,GPIO.LOW)
        GPIO.output(L2,GPIO.LOW)

@robot_speed.connect
def speed(app, speed):
    if speed == 0:
        print('speed up')
    elif speed == 1:
        print('speed down')