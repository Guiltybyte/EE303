import InOut as IO

orientation = 0


class dynamicActionList():
    "Maintains a list of action required to get from one node, to it's \
    adjacent nodes, changes instructions depending on the orientation"
    def __init__(self):
        global orientation
        self.ActionList = ({}, {}, {}, {}, {}, {}, {})
        self.update_ActionList()

    def orientation_switcher(self):
        print("orientation switcher")
        global orientation
        orientation = 1-orientation
        print(orientation)
        self.update_ActionList()

    def set_orientation(self, value):
        print("set_orientation = ", value)
        global orientation
        orientation = value
        self.update_ActionList()

    def update_ActionList(self):

        global orientation
        if orientation == 0:
            x = IO.bot_turnaround   # 180 turn in zero config
            y = NULL                # 180 turn in one config

        if orientation == 1:
            x = NULL
            y = IO.bot_turnaround

        self.ActionList[0][1] = (y, IO.bot_counterclockwise_0, IO.func_pass)
        self.ActionList[0][2] = (y, IO.func_pass, IO.func_pass)
        self.ActionList[0][4] = (x, IO.func_pass)

        self.ActionList[1][0] = (x, IO.bot_clockwise_1, IO.func_pass)
        self.ActionList[1][2] = (x, IO.bot_counterclockwise_0, IO.func_pass)  # noqa
        self.ActionList[1][3] = (y, IO.bot_clockwise_1, IO.func_pass)
        self.ActionList[1][4] = (y, IO.bot_counterclockwise_0, IO.func_pass)
        self.ActionList[1][5] = (y, IO.five, IO.func_pass)

        self.ActionList[2][0] = (x, IO.func_pass, IO.func_pass)
        self.ActionList[2][1] = (x, IO.bot_clockwise_0, IO.func_pass)
        self.ActionList[2][3] = (y, IO.func_pass)                       # yeehaw

        self.ActionList[3][1] = (y, IO.bot_counterclockwise_1, IO.func_pass)
        self.ActionList[3][2] = (x, IO.func_pass)                       # yeehaw
        self.ActionList[3][4] = (y, IO.func_pass, IO.func_pass)

        self.ActionList[4][0] = (y, IO.func_pass)
        self.ActionList[4][1] = (x, IO.bot_clockwise_1, IO.func_pass)  # noqa
        self.ActionList[4][3] = (x, IO.func_pass, IO.func_pass)

        self.ActionList[5][1] = None

        # start position, change to index 6 when adding dest 5 functionality
        self.ActionList[6][0] = (IO.func_pass, IO.func_pass)
        self.ActionList[6][4] = (IO.bot_turnaround, IO.func_pass)


# Hacky crap
def NULL():
    pass
