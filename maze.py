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

        def __init__(self, x: int, y: int, start=False, exit=False) -> None:
            """Initializes a cell.

            Creates a cell with every wall up and marks it as start or exit.
            Also creates the visited attribute for generation purposes.

            Args:
                x (int): X position of the cell in the maze.
                y (int): Y position of the cell in the maze.
                start (bool): Start of the maze. Defualts to False.
                exit (bool): End of the maze. Defaults to False.
            """
            self.x = x
            self.y = y

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
                start: bool = (x, y) == st
                exit: bool = (x, y) == ext
                self.grid[y].append(MazeGenerator.Cell(x, y, start, exit))
                
                if start:
                    self.start = self.grid[y][x]
                if exit:
                    self.exit = self.grid[y][x]

    def directions(self, cell: 'MazeGenerator.Cell') -> list[str]:
        dirs = []

        x, y = cell.x, cell.y

        if y > 0 and not self.grid[y - 1][x].visited:
            dirs.append('North')

        if x < self.width - 1 and not self.grid[y][x + 1].visited:
            dirs.append('East')

        if y < self.height - 1 and not self.grid[y + 1][x].visited:
            dirs.append('South')

        if x > 0 and not self.grid[y][x - 1].visited:
            dirs.append('West')

        return dirs

    def move(self, cell: 'MazeGenerator.Cell', direction: str) -> 'MazeGenerator.Cell':
        x, y = cell.x, cell.y

        if direction == 'North':
            next_cell = self.grid[y - 1][x]
            cell.walls['North'] = False
            next_cell.walls['South'] = False
            return next_cell

        if direction == 'East':
            next_cell = self.grid[y][x + 1]
            cell.walls['East'] = False
            next_cell.walls['West'] = False
            return next_cell

        if direction == 'South':
            next_cell = self.grid[y + 1][x]
            cell.walls['South'] = False
            next_cell.walls['North'] = False
            return next_cell

        if direction == 'West':
            next_cell = self.grid[y][x - 1]
            cell.walls['West'] = False
            next_cell.walls['East'] = False
            return next_cell

    # Depth-first Search algorithm - perfect maze
    def gen_dfs(self) -> None:
        rand.seed(42)
        history: list['MazeGenerator.Cell'] = [self.start]
        self.start.visited = True
        cell = self.start

        while True:
            if self.directions(cell):
                direction = rand.choice(self.directions(cell))
                cell = self.move(cell, direction)
                cell.visited = True
                history.append(cell)

            while not self.directions(cell) and history:
                cell = history.pop()

            if not history:
                break

    # Hunt and Kill algorith - perfect maze
    def gen_hak(self) -> None:
        pass

    # My own algorithm - imperfect maze
    def gen_imperfect(self) -> None:
        pass

    def to_hex_string(self) -> str:
        rows = []

        for y in range(self.height):
            row = ""
            for x in range(self.width):
                cell = self.grid[y][x]

                value = 0
                if cell.walls['North']:
                    value |= 1
                if cell.walls['East']:
                    value |= 2
                if cell.walls['South']:
                    value |= 4
                if cell.walls['West']:
                    value |= 8

                row += format(value, 'X')

            rows.append(row)

        return "\n".join(rows)

    def output(self, f: str, st: tuple, ext: tuple, sol: str) -> None:
        """Writes the hex maze to the output file.

        Iterates each cell of the maze and concatenates it to the maze_out
        variable, after iterating the entire maze, only then is the output
        file opened and the maze_out is written to it along with the rest of
        the maze information, such as the entry and exit locations and the
        solution for the maze created.

        Args:
            f (str): Path of maze output file.
            st (list[int, int]): x and y coordinates of maze start.
            ext (list[int, int]): x and y coordinates of maze exit.
            sol (str): Maze solution path.
        """
        maze_string = self.to_hex_string()

        maze_string += f'\n\n{st[0]},{st[1]}'
        maze_string += f'\n{ext[0]},{ext[1]}'
        maze_string += f'\n{sol}'

        with open(f, 'w') as output_file:
            output_file.write(maze_string)
