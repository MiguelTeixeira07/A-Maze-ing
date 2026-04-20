import random as rand


class MazeGenerator:
    """One maze cell.

    Attributes:
        width (int): Maze width.
        height (int): Maze height.
        grid (list[list[MazeGenerator.Cell]]): Matrix with every cell.
    """

    class Cell:
        """One maze cell.

        Attributes:
            start (bool): Start of the maze.
            exit (bool): Exit of the maze.
            walls (dict[str, bool]): Cell walls.
            hex (str): Hexadecimal representation of walls.
            visited (bool): Has the cell been visited on creation.
        """

        def __init__(self, start=False, exit=False) -> None:
            """Initializes a cell.

            Creates a cell with every wall up and marks it as start or exit.
            Also creates the visited attribute for generation purposes.

            Args:
                start (bool): Start of the maze. Defualts to False.
                exit (bool): End of the maze. Defaults to False.
            """
            self.start: bool = start
            self.exit: bool = exit

            self.walls: dict[str, bool] = {
                'North': True,
                'East': True,
                'South': True,
                'West': True
            }

            self.hex: str = 'F'

            self.visited: bool = False

    def __init__(self, w: int, h: int, st: list[int], ext: list[int]) -> None:
        """Initializes the maze.

        Makes a maze with every wall up
        Also marks the start and end cells

        Args:
            w (int): maze width.
            h (int): maze height.
            st (list[int, int]): x and y coordinates of maze start.
            ext (list[int, int]): x and y coordinates of maze exit.
        """
        self.width: int = w
        self.height: int = h

        self.grid: list[list[MazeGenerator.Cell]] = []
        for y in range(h):
            self.grid.append([])
            for x in range(w):
                start: bool = [x, y] == st
                exit: bool = [x, y] == ext
                self.grid[y].append(MazeGenerator.Cell(start, exit))

    # Depth-first Search algorithm - perfect maze
    def gen_dfs(self) -> None:
        pass

    # Hunt and Kill algorith - perfect maze
    def gen_hak(self) -> None:
        pass

    # My own algorithm - imperfect maze
    def gen_imperfect(self) -> None:
        pass

    def output(self, out_fp: str, st: tuple, ext: tuple, path: str) -> None:
        """Writes the hex maze to the output file.

        Iterates each cell of the maze and concatenates it to the maze_out
        variable, after iterating the entire maze, only then is the output
        file opened and the maze_out is written to it along with the rest of
        the maze information, such as the entry and exit locations and the
        solution for the maze created.

        Args:
            output_file_path (str): Path of maze output file.
            st (list[int, int]): x and y coordinates of maze start.
            ext (list[int, int]): x and y coordinates of maze exit.
            path (str): Path that solves the maze.
        """
        maze_out: str = '\n'.join([''.join([cell.hex for cell in row])
                                   for row in self.grid])

        maze_out += f'\n\n{st[0]},{st[1]}\n{ext[0]},{ext[1]}\n' + path

        with open(out_fp, 'w') as output_file:
            output_file.write(maze_out)
