import InOut as IO
from numpy import interp
from statistics import median
from simplepathfinder import Simplepathfinder


def interpolate_sensors():
    "read sensor values and return a weighted average based on \
    sensor distance from sensor"
    sensors = [IO.analogRead(IO.RIGHT_MOST_SENSOR),  # [0] right most
               IO.analogRead(IO.RIGHT_SENSOR),       # [1] middle-right
               IO.analogRead(IO.MIDDLE_SENSOR),      # [2] centre
               IO.analogRead(IO.LEFT_SENSOR),        # [3] middle-left
               IO.analogRead(IO.LEFT_MOST_SENSOR)]   # [4] left-most

    # checks if at intersection and stops if so
    Simplepathfinder.at_intersection(sensors)
    Simplepathfinder.exiting_junction()
    # index matches index of corresponding sensor
    # weights are assigned by pixel distance from centre
    # by convention, right of centre sensors are weighted negatively
    weights = [-32, -16, 0, 16, 32]

    # Calculate the weighted average
    numerator = 0
    for i in range(5):
        numerator += sensors[i] * weights[i]
    denominator = sum(sensors)

    return numerator / denominator


def motor_driver(position):
    "interprets interpolated position value and drives motors accordingly"
    MIN_SPEED = 80          # lower speed recommended when stopping required
    MAX_SPEED = 1023

    if position < 0:        # right turn required
        position = -position
        turn_speed = interp(position, [0, 32], [MIN_SPEED, MAX_SPEED])
        IO.bot_forward(turn_speed, MIN_SPEED)
    else:                   # left turn required
        turn_speed = interp(position, [0, 32], [MIN_SPEED, MAX_SPEED])
        IO.bot_forward(MIN_SPEED, turn_speed)


def line_follower():
    "implements line following behaviour"
    input_buffer = []
    for i in range(50):
        input_buffer.append(interpolate_sensors())
    motor_driver(median(input_buffer))  # median reduces influence of outliers
