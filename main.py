from linefollower import line_follower
import InOut as IO
from simplepathfinder import Simplepathfinder
from communicator import get_random_destination

# pass in as function names without arg brackets
task3_directions = [IO.func_pass,
                    IO.dest_stop,
                    IO.func_pass,
                    IO.bot_counterclockwise,
                    IO.dest_stop,
                    IO.bot_turnaround,
                    IO.bot_counterclockwise,
                    IO.dest_stop,
                    IO.func_pass,
                    IO.dest_stop,
                    IO.func_pass,
                    IO.func_pass,
                    IO.dest_stop]
# task3 = Simplepathfinder(task3_directions)

task4_directions = [IO.bot_turnaround,
                    IO.dest_stop,
                    IO.func_pass,
                    IO.func_pass,
                    IO.dest_stop,
                    IO.bot_turnaround,
                    IO.bot_counterclockwise,
                    IO.dest_stop,
                    IO.bot_turnaround,
                    IO.five]


def setup():
    get_random_destination()


setup()
task4 = Simplepathfinder(task4_directions)


# loop
while True:
    line_follower()
