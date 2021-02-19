import InOut as IO
from time import sleep

actions = []
action_counter = 0


# this is an OOPomination
class Simplepathfinder():
    def __init__(self, new_actions):
        global actions
        actions = new_actions
        global action_counter
        action_counter = 0
        Simplepathfinder.navigate()  # first action performed at startup

    def at_intersection(sensors, IGNORE_JUNCTION=False):
        "checks if bot should stop, can be set to ignore the dest 1 junctions"
        intersection = True
        for sensor in sensors:
            if sensor < 253:
                intersection = False

        # ignore  the junctions 
        if IGNORE_JUNCTION:
            if IO.analogRead(IO.DISTANCE_SENSOR) in range(276, 292):
                intersection = False

        # stops bot and executes current action in actions list
        if intersection:
            Simplepathfinder.navigate()
        return intersection

    def navigate():
        IO.bot_stop()
        global action_counter
        # print(action_counter)
        actions[action_counter]()
        action_counter += 1

    # nesscesary because coming out of junction 1 sensors are not guaranteed
    # to detect as a junction, so slamming against the wall is the next 
    # detection
    def exiting_junction():
        if IO.analogRead(IO.DISTANCE_SENSOR) <= 32:
            Simplepathfinder.navigate()
