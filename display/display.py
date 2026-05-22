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
        """Returns the main maze output string for the user.

        Goes through the whole maze to append each cell's walls to the output
        string.
        It does this by going through each row tiwce, one to append the top
        wall of each cell, and another one to append both side's walls. After
        going through the entire maze, it appends a full line on the bottom to
        serve as the bottom wall for the bottom-most cells.
        This way of printing works because wach cell shares walls, so printing
        only the top wall of each cell hence printing the bottom wall too.

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
        """Changes the colors of each part of the maze.

        Picks a random color excluding the color passed on the arguments and
        every past color picked on this iteration.

        Attributes:
            exclude (Opt[str]): One color that will not be repeated.
            Defaults to None.
        """
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
