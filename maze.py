import random as rand


class Maze:
    """One maze cell.

    Attributes:
        width (int): Maze width.
        height (int): Maze height.
        start (Maze.Cell): Start of the maze
        exit (Maze.Cell): Exit of the maze
        grid (list[list[Maze.Cell]]): Matrix with every cell.
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
        pattern_cells = (
            [((w - 7) // 2), ((h - 5) // 2)], # left of 4
            [((w - 7) // 2) + 4, ((h - 5) // 2)], # top of 2
            [((w - 7) // 2) + 5, ((h - 5) // 2)], # top of 2
            [((w - 7) // 2) + 6, ((h - 5) // 2)], # top of 2

            [((w - 7) // 2), ((h - 5) // 2) + 1], # left of 4
            [((w - 7) // 2) + 6, ((h - 5) // 2) + 1], # right of 2

            [((w - 7) // 2), ((h - 5) // 2) + 2], # middle of 4
            [((w - 7) // 2) + 1, ((h - 5) // 2) + 2], # middle of 4
            [((w - 7) // 2) + 2, ((h - 5) // 2) + 2], # middle of 4
            [((w - 7) // 2) + 4, ((h - 5) // 2) + 2], # middle of 2
            [((w - 7) // 2) + 5, ((h - 5) // 2) + 2], # middle of 2
            [((w - 7) // 2) + 6, ((h - 5) // 2) + 2], # middle of 2

            [((w - 7) // 2) + 2, ((h - 5) // 2) + 3], # right of 4
            [((w - 7) // 2) + 4, ((h - 5) // 2) + 3], # left of 2

            [((w - 7) // 2) + 2, ((h - 5) // 2) + 4], # right of 4
            [((w - 7) // 2) + 4, ((h - 5) // 2) + 4], # bottom of 2
            [((w - 7) // 2) + 5, ((h - 5) // 2) + 4], # bottom of 2
            [((w - 7) // 2) + 6, ((h - 5) // 2) + 4] # bottom of 2
        )
        self.width: int = w
        self.height: int = h

        self.grid: list[list[Maze.Cell]] = []
        for y in range(h):
            self.grid.append([])
            for x in range(w):
                start: bool = (x, y) == st
                exit: bool = (x, y) == ext
                self.grid[y].append(Maze.Cell(x, y, start, exit))

                if [x, y] in pattern_cells:
                    self.grid[y][x].visited = True

                if start:
                    self.start = self.grid[y][x]
                if exit:
                    self.exit = self.grid[y][x]

    def directions(self, cell: 'Maze.Cell') -> list[str]:
        """Gets all valid directions.

        Checks each of the 4 neighbouring cells and adds them to the list if
        not visited, so that every cell that was visited is not included, this
        is what allows this algorithm to generate a perfect maze.

        Args:
            cell (Maze.Cell): Current cell.

        Returns:
            list[str]: List of every valid direction to move to.
        """
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

    def move(self, cell: 'Maze.Cell', direction: str) -> 'Maze.Cell':
        """Moves a cell to a specified direction.

        Determines what the next cell is, breaks the wall in that direction
        and breaks the next cell's wall in the opposite direction.

        Args:
            cell (Maze.Cell): Current cell.
            direction (str): Direction to move the cell to.

        Returns:
            Maze.Cell: New cell.
        """
        x, y = cell.x, cell.y
        next_cell = cell

        match direction:
            case 'North':
                next_cell = self.grid[y - 1][x]
                cell.walls['North'] = False
                next_cell.walls['South'] = False

            case 'East':
                next_cell = self.grid[y][x + 1]
                cell.walls['East'] = False
                next_cell.walls['West'] = False

            case 'South':
                next_cell = self.grid[y + 1][x]
                cell.walls['South'] = False
                next_cell.walls['North'] = False

            case 'West':
                next_cell = self.grid[y][x - 1]
                cell.walls['West'] = False
                next_cell.walls['East'] = False

        return next_cell

    # Depth-first Search algorithm - perfect maze
    def gen_dfs(self) -> None:
        """Generates a perfect maze with the depth-first-search algorithm.

        Starts the generation on the entry of the maze.
        While the maze is not fully generated, the algorithm will pick a
        random direction and move there if it has not been visited yet.
        When the algorithm gets to a dead-end, it traces back the path it made
        there until it finds a cell that has neighbours which have not been
        visited yet.
        If it backtracks all the way back to the start, then it means all the
        cells have been visited, therefore the maze has been fully generated,
        with all cells accessible.
        """
        from display.display import printing_walls
        import time
        import os
        # rand.seed(42)
        history: list['Maze.Cell'] = [self.start]
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

            os.system('clear')
            print(printing_walls(self, self.width, self.height), end='', flush=True)
            time.sleep(0.01667)

            if not history:
                break
        print()

    # Hunt and Kill algorith - perfect maze
    def gen_hak(self) -> None:
        # rand.seed(42)
        self.start.visited = True
        cell = self.start

        while True:
            if self.directions(cell):
                direction = rand.choice(self.directions(cell))
                cell = self.move(cell, direction)
                cell.visited = True

            while not self.directions(cell):
                found = False
                for y in range(self.height):
                    for x in range(self.width):
                        if self.grid[y][x].visited:
                            cell = self.grid[y][x]
                            found = True
                            break
                    if found:
                        break

                return

    # My own algorithm - imperfect maze
    def gen_imperfect(self) -> None:
        pass

    def to_hex_string(self) -> str:
        rows = []

        for y in range(self.height):
            row = ''
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

                cell.hex = format(value, 'X')
                row += cell.hex

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
