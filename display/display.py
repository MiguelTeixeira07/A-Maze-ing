from .walls import Walls
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
    for row in maze.grid:
        for i in range(2):
            place_in_row = 0

            output += gcolor + '██'
            for cell in row:
                if i == 0:
                    if cell.walls['North']:
                        output += gcolor + str(Walls.TOP)
                    else:
                        output += gcolor + str(Walls.LEFT_AND_RIGHT)
                else:
                    if all(wall for wall in cell.walls.values()) and cell.visited:
                        output += '█' + logo_color + '███' + gcolor + '█'
                    else:
                        if cell.walls['East'] and cell.walls['West']:
                            if cell in solution:
                                output += '█' + path_color + '███' + gcolor + '█'
                            else:
                                output += gcolor + str(Walls.LEFT_AND_RIGHT)
                        else:
                            if cell.walls['West']:
                                if cell in solution:
                                    output += '█' + path_color + '███ '
                                else:
                                    output += gcolor + str(Walls.LEFT)
                            elif cell.walls['East']:
                                if cell in solution:
                                    output += path_color + ' ███' + gcolor + '█'
                                else:
                                    output += gcolor + str(Walls.RIGHT)
                            else:
                                if cell in solution:
                                    output += path_color + ' ███ '
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


def print_maze(maze: Maze, solution):
    width = maze.width  # O width era parametro mas como o maze ja tem width eu tirei
    grid_color = random_color()  # random_color agora leva como argumentos as cores que nao queres que sejam escolhidas
    logo_color = random_color(grid_color)
    entry_color = random_color(grid_color, logo_color)
    exit_color = random_color(grid_color, logo_color, entry_color)
    path_color = random_color(grid_color, logo_color, entry_color, exit_color)

    output = printing_walls(
        maze,
        width,
        solution,
        grid_color,
        logo_color,
        entry_color,
        exit_color,
        path_color
    )
    return output
