from enum import Enum


class Walls(Enum):
    EMPTY = "     "

    TOP = "█████"

    RIGHT = "    █"

    LEFT = "█    "

    LEFT_AND_RIGHT = "█   █"

    def __str__(self):
        return self.value
