from .walls import Walls
from maze import Maze


def printing_walls(maze: Maze, width: int, height: int) -> None:
    for row in maze.grid:
        for i in range(2):
            place_in_row = 0

            print('██', end='')
            for cell in row:
                if i == 0:
                    if cell.walls['North']:
                        print(Walls.TOP, end='')
                    else:
                        print(Walls.LEFT_AND_RIGHT, end='')
                else:
                    if cell.walls['East'] and cell.walls['West']:
                        print(Walls.LEFT_AND_RIGHT, end='')
                    else:
                        if cell.walls['West']:
                            print(Walls.LEFT, end='')
                        elif cell.walls['East']:
                            print(Walls.RIGHT, end='')
                        else:
                            print(Walls.EMPTY, end='')

                if place_in_row == width - 1:
                    print('██')

                place_in_row += 1

    print('██', end='')
    for _ in range(width):
        print('█████', end='')
    print('██')

    print()


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
