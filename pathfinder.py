import InOut as IO


class Pathfinder():
    # index holds list of nodes adjacent mode name == index
    # at any destination, bot should turn so that it faces normal direction
    # must go to destination 1 to go to destination 5
    #do not need to return from destination 5

    #            # destination 0
    trackinfo = [[[1, "linefollow", "stop", "counterclockwise", "linefollow", "stop"],                      # noqa
                  [2, "linefollow", "stop", "linefollow", "stop"],
                  [4, "turnaround", "linefollow", "stop"]],
                 # destination 1
                 [[5, "foward", "stop"],
                  [2, "turnaround", "linefollow", "stop", "counterclockwise", "linefollow","stop"],         # noqa
                  [0, "turnaround", "linefollow", "clockwise", "linefollow", "stop", "turnaround"]],        # noqa
                 # destination 2
                 [[1, "turnaround", "linefollow", "stop", "clockwise", "linefollow", "stop"],               # noqa
                  [3, "linefollow", "stop"],
                  [0, "turnaround", "linefollow", "stop", "linefollow", "stop"]],                           # noqa
                 # destination 3
                 [[1, "linefollow", "stop", "counterclockwise", "linefollow", "stop", "turnaround" ],       # noqa
                  [4, "linefollow", "stop", "linefollow", "stop"]],
                 # destination 4
                 [[1, "turnaround", "linefollow", "stop", "clockwise", "linefollow", "stop", "turnaround"], # noqa
                  [3, "turnaround", "linefollow", "stop", "linefollow", "stop", "turnaround"],              # noqa
                  [0, "linefollow", "stop"]],
                 ]

    def __init__(self, path):
        self.instructions = bruteforce_path(path)

    def bruteforce_path(path):
        for i in path:
            for visible_destination in trackinfo[i]:
