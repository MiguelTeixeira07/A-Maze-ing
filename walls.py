from enum import Enum


class Walls(Enum):
    EMPTY = ' '
    TOP_LEFT = '╔'
    H_LINE = '═'
    TOP_RIGHT = '╗'
    V_LINE = '║'
    BOTTOM_LEFT = '╚'
    BOTTOM_RIGHT = '╝'
    TOP_JUNC = '╦'
    RIGHT_JUNC = '╣'
    LEFT_JUNC = '╠'
    BOTTOM_JUNC = '╩'
    ALL_JUNC = '╬'

    def __str__(self):
        return self.value


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
