from typing import Optional as Opt
from collections.abc import Callable
from .walls import Walls
from mazegen.maze import Maze
from .colors import random_color


class Display:
    colors: dict[str, str] = {}

    @classmethod
    def print_maze(
        cls,
        maze: Maze,
        solution: list[Maze.Cell]
    ) -> str:
        """
        The method responsible to return the string with the maze user output

        Runs through 3 loops:\n
        The first for every row in the grid\n
        The second to make sure the space inside the grid is printed\n
        The third (inner) determines which characters and colors should be
        added to the output string.

        Args:
            maze (Maze): class Maze containing all its attributes.
            maze.width (int): Maze width.j
            solution (list[Maze.Cell]): Cells that form the solution path.
            g_color (str): the color the grid will be displayed.
            logo_color (str): the color the logo will be displayed.
            entry_color (str): the color the entry will be displayed.
            exit_color (str): the color the exit will be displayed.
            path_color (str): the color the path will be displayed.

        Returns:
            output: str
        """

        output: str = ''
        east_west: Callable[[str], str] = lambda c: (
            '█' + c + '███' + cls.colors['g_color'] + '█'
        )
        west: Callable[[str], str] = lambda c: (
            '█' + c + '███ '
        )
        east: Callable[[str], str] = lambda c: (
            c + ' ███' + cls.colors['g_color'] + '█'
        )
        none: Callable[[str], str] = lambda c: (
            c + ' ███ '
        )

        for row in maze.grid:
            for i in range(2):
                place_in_row: int = 0

                output += cls.colors['g_color'] + '██'
                for cell in row:
                    if i == 0:
                        if cell.walls['North']:
                            output += cls.colors['g_color']
                            output += str(Walls.TOP)
                        else:
                            output += cls.colors['g_color']
                            output += str(Walls.LEFT_AND_RIGHT)
                    else:
                        if all(w for w in cell.walls.values()):
                            output += east_west(cls.colors['logo_color'])
                        else:
                            if cell.walls['East'] and cell.walls['West']:
                                if cell.start:
                                    output += east_west(
                                        cls.colors['entry_color']
                                    )
                                elif cell.exit:
                                    output += east_west(
                                        cls.colors['exit_color']
                                    )
                                elif cell in solution:
                                    output += east_west(
                                        cls.colors['path_color']
                                    )
                                else:
                                    output += cls.colors['g_color']
                                    output += str(Walls.LEFT_AND_RIGHT)
                            else:
                                if cell.walls['West']:
                                    if cell.start:
                                        output += west(
                                            cls.colors['entry_color']
                                        )
                                    elif cell.exit:
                                        output += west(
                                            cls.colors['exit_color']
                                        )
                                    elif cell in solution:
                                        output += west(
                                            cls.colors['path_color']
                                        )
                                    else:
                                        output += cls.colors['g_color']
                                        output += str(Walls.LEFT)

                                elif cell.walls['East']:
                                    if cell.start:
                                        output += east(
                                            cls.colors['entry_color']
                                        )
                                    elif cell.exit:
                                        output += east(
                                            cls.colors['exit_color']
                                        )
                                    elif cell in solution:
                                        output += east(
                                            cls.colors['path_color']
                                        )
                                    else:
                                        output += cls.colors['g_color']
                                        output += str(Walls.RIGHT)
                                else:
                                    if cell.start:
                                        output += none(
                                            cls.colors['entry_color']
                                        )
                                    elif cell.exit:
                                        output += none(
                                            cls.colors['exit_color']
                                        )
                                    elif cell in solution:
                                        output += none(
                                            cls.colors['path_color']
                                        )
                                    else:
                                        output += cls.colors['g_color']
                                        output += str(Walls.EMPTY)

                    if place_in_row == maze.width - 1:
                        output += '██\n'

                    place_in_row += 1

        output += '██'
        for _ in range(maze.width):
            output += '█████'
        output += '██'

        return output

    @classmethod
    def set_colors(cls, exclude: Opt[str] = None) -> None:
        cls.colors['g_color'] = random_color(
            exclude
        )
        cls.colors['logo_color'] = random_color(
            cls.colors['g_color']
        )
        cls.colors['path_color'] = random_color(
            cls.colors['g_color'],
            cls.colors['logo_color']
        )
        cls.colors['entry_color'] = random_color(
            cls.colors['g_color'],
            cls.colors['logo_color'],
            cls.colors['path_color']
        )
        cls.colors['exit_color'] = random_color(
            cls.colors['g_color'],
            cls.colors['logo_color'],
            cls.colors['path_color'],
            cls.colors['entry_color']
        )


Display.set_colors()
