from enum import Enum


class Walls(Enum):
    EMPTY = "    "

    TOP = ("▀▀▀▀", "    ")

    RIGHT = ("   █", "   █")

    TOP_RIGHT = ("▀▀▀█", "   █")

    BOTTOM = ("    ", "▄▄▄▄")

    TOP_BOTTOM = ("▀▀▀▀", "▄▄▄▄")

    RIGHT_BOTTOM = ("   █", "▄▄▄█")

    TOP_RIGHT_BOTTOM = ("▀▀▀█", "▄▄▄█")

    LEFT = ("█   ", "█   ")

    TOP_LEFT = ("█▀▀▀", "█   ")

    RIGHT_LEFT = ("█  █", "█  █")

    TOP_RIGHT_LEFT = ("█▀▀█", "█  █")

    BOTTOM_LEFT = ("█   ", "█▄▄▄")

    TOP_BOTTOM_LEFT = ("█▀▀▀", "█▄▄▄")

    RIGHT_BOTTOM_LEFT = ("█  █", "█▄▄█")

    ALL = ("█▀▀█", "█▄▄█")

    def __str__(self):
        return self.value


if __name__ == '__main__':
    print(Walls.TOP_LEFT, Walls.H_LINE, Walls.TOP_RIGHT, sep='')
    print(Walls.V_LINE, ' ', Walls.V_LINE, sep='')
    print(Walls.BOTTOM_LEFT, Walls.H_LINE, Walls.BOTTOM_RIGHT, sep='')

    print('\n')

    print(Walls.TOP_LEFT, Walls.H_LINE, Walls.TOP_JUNC, sep='', end='')
    print(Walls.H_LINE, Walls.TOP_RIGHT, sep='')
    print(Walls.V_LINE, ' ', Walls.V_LINE, ' ', Walls.V_LINE, sep='')
    print(Walls.BOTTOM_LEFT, Walls.H_LINE, Walls.BOTTOM_JUNC, sep='', end='')
    print(Walls.H_LINE, Walls.BOTTOM_RIGHT, sep='')

    print('\n')

    print(Walls.TOP_LEFT, Walls.H_LINE, Walls.TOP_JUNC, sep='', end='')
    print(Walls.H_LINE, Walls.TOP_RIGHT, sep='')
    print(Walls.V_LINE, ' ', Walls.V_LINE, ' ', Walls.V_LINE, sep='')
    print(Walls.LEFT_JUNC, Walls.H_LINE, Walls.ALL_JUNC, sep='', end='')
    print(Walls.H_LINE, Walls.RIGHT_JUNC, sep='')

    print(Walls.V_LINE, ' ', Walls.V_LINE, ' ', Walls.V_LINE, sep='')
    print(Walls.BOTTOM_LEFT, Walls.H_LINE, Walls.BOTTOM_JUNC, sep='', end='')
    print(Walls.H_LINE, Walls.BOTTOM_RIGHT, sep='')
