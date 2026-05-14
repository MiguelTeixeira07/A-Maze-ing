from .walls import Walls
from maze import Maze
from .colors import random_color

class Display:
    g_color: str
    logo_color: str
    path_color: str
    entry_color: str
    exit_color: str

    def print_maze(
            self,
            maze: Maze,
            solution: list[Maze.Cell]) -> str:
        """
                The method responsible to return the string with the correct output

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

        output = ''
        east_west = lambda c: '█' + c + '███' + self.g_color + '█'
        west = lambda c: '█' + c + '███ '
        east = lambda c: c + ' ███' + self.g_color + '█'
        none = lambda c: c + ' ███ '

        for row in maze.grid:
            for i in range(2):
                place_in_row = 0

                output += self.g_color + '██'
                for cell in row:
                    if i == 0:
                        if cell.walls['North']:
                            output += self.g_color + str(Walls.TOP)
                        else:
                            output += self.g_color + str(Walls.LEFT_AND_RIGHT)
                    else:
                        if all(w for w in cell.walls.values()) and cell.visited:
                            output += east_west(self.logo_color)
                        else:
                            if cell.walls['East'] and cell.walls['West']:
                                if cell.start:
                                    output += east_west(self.entry_color)
                                elif cell.exit:
                                    output += east_west(self.exit_color)
                                elif cell in solution:
                                    output += east_west(self.path_color)
                                else:
                                    output += self.g_color + str(Walls.LEFT_AND_RIGHT)
                            else:
                                if cell.walls['West']:
                                    if cell.start:
                                        output += west(self.entry_color)
                                    elif cell.exit:
                                        output += west(self.exit_color)
                                    elif cell in solution:
                                        output += west(self.path_color)
                                    else:
                                        output += self.g_color + str(Walls.LEFT)

                                elif cell.walls['East']:
                                    if cell.start:
                                        output += east(self.entry_color)
                                    elif cell.exit:
                                        output += east(self.exit_color)
                                    elif cell in solution:
                                        output += east(self.path_color)
                                    else:
                                        output += self.g_color + str(Walls.RIGHT)
                                else:
                                    if cell.start:
                                        output += none(self.entry_color)
                                    elif cell.exit:
                                        output += none(self.exit_color)
                                    elif cell in solution:
                                        output += none(self.path_color)
                                    else:
                                        output += self.g_color + str(Walls.EMPTY)

                    if place_in_row == maze.width - 1:
                        output += '██\n'

                    place_in_row += 1

        output += '██'
        for _ in range(maze.width):
            output += '█████'
        output += '██'

        return output

    
    @classmethod
    def set_colors(cls, exclude=None):
        cls.g_color = random_color(exclude)
        cls.logo_color = random_color(cls.g_color)
        cls.path_color = random_color(cls.g_color, cls.logo_color)
        cls.entry_color = random_color(cls.g_color, cls.logo_color, cls.path_color)
        cls.exit_color = random_color(cls.g_color, cls.logo_color, cls.path_color, cls.entry_color)

Display.set_colors()
