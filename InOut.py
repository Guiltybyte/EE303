import numpy as np
from time import sleep

pins = np.memmap("bots/001/pins.dat", dtype=np.uint32, mode="r+", shape=(41,))

DISTANCE_SENSOR = 1
RIGHT_MOST_SENSOR = 8
RIGHT_SENSOR = 9
MIDDLE_SENSOR = 11
LEFT_SENSOR = 13
LEFT_MOST_SENSOR = 14
LEFT_MOTOR_PHASE = 37
RIGHT_MOTOR_PHASE = 39
LEFT_MOTOR_SPEED = 38
RIGHT_MOTOR_SPEED = 40


def analogRead(pin):
    return pins[pin]


def analogWrite(pin, value):
    if value < 0 or value > 1023:
        raise ValueError
    pins[pin] = value


def digitalRead(pin):
    return pins[pin]


def digitalWrite(pin, value):
    if value not in (0, 1):
        raise ValueError
    pins[pin] = value


def bot_stop():
    "Stops Robot and resets bot to forward, returns True when complete"
    analogWrite(RIGHT_MOTOR_SPEED, 0)
    analogWrite(LEFT_MOTOR_SPEED, 0)
    digitalWrite(RIGHT_MOTOR_PHASE, 1)
    digitalWrite(LEFT_MOTOR_PHASE, 1)
    return True


def dest_stop():
    bot_stop()
    sleep(2)


def bot_forward(rspeed, lspeed):
    "sets bot to forward at speed"
    digitalWrite(LEFT_MOTOR_PHASE, 1)
    digitalWrite(RIGHT_MOTOR_PHASE, 1)
    analogWrite(LEFT_MOTOR_SPEED, lspeed)
    analogWrite(RIGHT_MOTOR_SPEED, rspeed)


def bot_clockwise():
    "turns bot pi/2 rads clockwise"
    digitalWrite(LEFT_MOTOR_PHASE, 0)
    digitalWrite(RIGHT_MOTOR_PHASE, 1)
    analogWrite(LEFT_MOTOR_SPEED, 50)
    analogWrite(RIGHT_MOTOR_SPEED, 50)
    sleep(1.6)
    return True


def bot_counterclockwise():
    "turns bot pi/2 rads counter-clockwise"
    digitalWrite(LEFT_MOTOR_PHASE, 1)
    digitalWrite(RIGHT_MOTOR_PHASE, 0)
    analogWrite(LEFT_MOTOR_SPEED, 50)
    analogWrite(RIGHT_MOTOR_SPEED, 50)
    sleep(1.6)
    return True


def bot_turnaround():
    "turns bot around pi rads, clockwise"
    bot_clockwise()
    bot_clockwise()
    return True


def func_pass():
    bot_forward(100, 100)
    sleep(500e-3)


# might need to write a diff method for each possible approach to five
def five():
    bot_forward(100, 100)
    while analogRead(DISTANCE_SENSOR) > 32:
        print(analogRead(DISTANCE_SENSOR))
