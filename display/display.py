from typing import List, Tuple
from colorama import Style, Fore, init
from .walls import Walls
from .colors import random_color
from maze import Maze
from colorama import Fore, init
from .colors import random_color


def printing_walls(
        maze: Maze,
        width: int,
        solution: list[Maze.Cell],
        gcolor: str,
        logo_color: str,
        entry_color: str,
        exit_color: str,
        path_color: str) -> str:

    output = ''
    east_west = lambda c: '█' + c + '███' + gcolor + '█'
    west = lambda c: '█' + c + '███ '
    east = lambda c: c + ' ███' + gcolor + '█'
    none = lambda c: c + ' ███ '

    for row in maze.grid:
        for i in range(2):
            place_in_row = 0
            line = ''

            output += gcolor + '██'
            for cell in row:
                if i == 0:
                    if cell.walls['North']:
                        output += gcolor + str(Walls.TOP)
                    else:
                        output += gcolor + str(Walls.LEFT_AND_RIGHT)
                else:
                    if all(w for w in cell.walls.values()) and cell.visited:
                        output += east_west(logo_color)
                    else:
                        if cell.walls['East'] and cell.walls['West']:
                            if cell.start:
                                output += east_west(entry_color)
                            elif cell.exit:
                                output += east_west(exit_color)
                            elif cell in solution:
                                output += east_west(path_color)
                            else:
                                output += gcolor + str(Walls.LEFT_AND_RIGHT)
                        else:
                            if cell.walls['West']:
                                if cell.start:
                                    output += west(entry_color)
                                elif cell.exit:
                                    output += west(exit_color)
                                elif cell in solution:
                                    output += west(path_color)
                                else:
                                    output += gcolor + str(Walls.LEFT)

                            elif cell.walls['East']:
                                if cell.start:
                                    output += east(entry_color)
                                elif cell.exit:
                                    output += east(exit_color)
                                elif cell in solution:
                                    output += east(path_color)
                                else:
                                    output += gcolor + str(Walls.RIGHT)
                            else:
                                if cell.start:
                                    output += none(entry_color)
                                elif cell.exit:
                                    output += none(exit_color)
                                elif cell in solution:
                                    output += none(path_color)
                                else:
                                    output += gcolor + str(Walls.EMPTY)

                if place_in_row == width - 1:
                    output += '██\n'

                place_in_row += 1

    output += '██'
    for _ in range(width):
        output += '█████'
    output += '██'

    return output


def print_maze(
        maze: Maze,
        solution: list[Maze.Cell],
        grid_color: str,
        logo_color: str,
        entry_color: str,
        exit_color: str,
        path_color: str) -> str:

    width: int = maze.width

    return printing_walls(
        maze,
        width,
        solution,
        grid_color,
        logo_color,
        entry_color,
        exit_color,
        path_color
    )
