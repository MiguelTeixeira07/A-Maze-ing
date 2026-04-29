from .walls import Walls
from maze import Maze


def printing_walls(maze: Maze, width: int, height: int) -> str:
    output = ''
    for row in maze.grid:
        for i in range(2):
            place_in_row = 0

            output += '██'
            for cell in row:
                if i == 0:
                    if cell.walls['North']:
                        output += str(Walls.TOP)
                    else:
                        output += str(Walls.LEFT_AND_RIGHT)
                else:
                    if cell.walls['East'] and cell.walls['West']:
                        output += str(Walls.LEFT_AND_RIGHT)
                    else:
                        if cell.walls['West']:
                            output += str(Walls.LEFT)
                        elif cell.walls['East']:
                            output += str(Walls.RIGHT)
                        else:
                            output += str(Walls.EMPTY)

                if place_in_row == width - 1:
                    output += '██\n'

                place_in_row += 1

    output += '██'
    for _ in range(width):
        output += '█████'
    output += '██'

    return output


def print_maze(maze: Maze, width: int, height: int):
    pattern = [
            '██  ██   ██████ ',
            '██  ██  ██    ██',
            '██  ██       ██ ',
            '██████     ███  ',
            '    ██    ██    ',
            '    ██   ██     ',
            '    ██  ████████'
            ]
    printing_walls(maze, width, height)
