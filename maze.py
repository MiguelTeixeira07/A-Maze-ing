import random as rand
import time
import sys
from collections.abc import Callable


class Maze:
    """One maze cell.

    Attributes:
        width (int): Maze width
        height (int): Maze height
        start (Maze.Cell): Start of the maze
        exit (Maze.Cell): Exit of the maze
        grid (list[list[Maze.Cell]]): Matrix with every cell
        sv (bool): Was this cell visited on the algorithm that solves the maze
    """
    class Cell:
        """One maze cell.

        Attributes:
            start (bool): Start of the maze
            exit (bool): Exit of the maze
            walls (dict[str, bool]): Cell walls
            hex (str): Hexadecimal representation of walls
            visited (bool): Has the cell been visited on creation
            sv (bool): Has this cell been visited while solving
        """
        def __init__(
            self,
            x: int,
            y: int,
            start: bool = False,
            exit: bool = False
        ) -> None:
            """Initializes a cell.

            Creates a cell with every wall up and marks it as start or exit.
            Also creates the visited attribute for generation purposes.

            Args:
                x (int): X position of the cell in the maze
                y (int): Y position of the cell in the maze
                start (bool): Start of the maze. Defualts to False
                exit (bool): End of the maze. Defaults to False
            """
            self.x: int = x
            self.y: int = y

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

            self.sv: bool = False

    def __init__(self, w: int, h: int, st: list[int], ext: list[int]) -> None:
        """Initializes the maze.

        Makes a maze with every wall up
        Also marks the start and end cells

        Args:
            w (int): maze width
            h (int): maze height
            st (list[int, int]): x and y coordinates of maze start
            ext (list[int, int]): x and y coordinates of maze exit
        """
        self.pattern_cells: list[list[int]] = [
            [((w - 7) // 2), ((h - 5) // 2)],  # left of 4
            [((w - 7) // 2) + 4, ((h - 5) // 2)],  # top of 2
            [((w - 7) // 2) + 5, ((h - 5) // 2)],  # top of 2
            [((w - 7) // 2) + 6, ((h - 5) // 2)],  # top of 2

            [((w - 7) // 2), ((h - 5) // 2) + 1],  # left of 4
            [((w - 7) // 2) + 6, ((h - 5) // 2) + 1],  # right of 2

            [((w - 7) // 2), ((h - 5) // 2) + 2],  # middle of 4
            [((w - 7) // 2) + 1, ((h - 5) // 2) + 2],  # middle of 4
            [((w - 7) // 2) + 2, ((h - 5) // 2) + 2],  # middle of 4
            [((w - 7) // 2) + 4, ((h - 5) // 2) + 2],  # middle of 2
            [((w - 7) // 2) + 5, ((h - 5) // 2) + 2],  # middle of 2
            [((w - 7) // 2) + 6, ((h - 5) // 2) + 2],  # middle of 2

            [((w - 7) // 2) + 2, ((h - 5) // 2) + 3],  # right of 4
            [((w - 7) // 2) + 4, ((h - 5) // 2) + 3],  # left of 2

            [((w - 7) // 2) + 2, ((h - 5) // 2) + 4],  # right of 4
            [((w - 7) // 2) + 4, ((h - 5) // 2) + 4],  # bottom of 2
            [((w - 7) // 2) + 5, ((h - 5) // 2) + 4],  # bottom of 2
            [((w - 7) // 2) + 6, ((h - 5) // 2) + 4]  # bottom of 2
        ]
        self.width: int = w
        self.height: int = h

        self.grid: list[list[Maze.Cell]] = []
        for y in range(h):
            self.grid.append([])
            for x in range(w):
                start: bool = (x, y) == tuple(st)
                exit: bool = (x, y) == tuple(ext)
                self.grid[y].append(Maze.Cell(x, y, start, exit))

                if [x, y] in self.pattern_cells:
                    self.grid[y][x].visited = True

                if start:
                    if [x, y] in self.pattern_cells:
                        print('Maze entry is inside the pattern cells.')
                        sys.exit(0)
                    self.start: 'Maze.Cell' = self.grid[y][x]
                if exit:
                    if [x, y] in self.pattern_cells:
                        print('Maze exit is inside the pattern cells.')
                        sys.exit(0)
                    self.exit: 'Maze.Cell' = self.grid[y][x]

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

        x: int = cell.x
        y: int = cell.y

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
        x: int = cell.x
        y: int = cell.y
        next_cell: 'Maze.Cell' = cell

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
        with all cells accessible (for the sole exception of the 42 pattern
        cells).
        """
        from display.display import Display

        history: list['Maze.Cell'] = [self.start]
        self.start.visited = True
        cell: 'Maze.Cell' = self.start

        while True:
            if self.directions(cell):
                direction: str = rand.choice(self.directions(cell))
                cell = self.move(cell, direction)
                cell.visited = True
                history.append(cell)

            while not self.directions(cell) and history:
                cell = history.pop()

            print('\033[H')
            print('Maze generation algorithm: Depth-first search')
            print(
                Display.print_maze(self, []),
                end='',
                flush=True
            )
            time.sleep(0.01)

            if not history:
                break

        # This is only here to make sure the 2 from 42 is not closed off
        self.gen_hak()

    # Hunt and Kill algorith - perfect maze
    def gen_hak(self) -> None:
        """Generates a perfect maze with the hunt-and-kill algorithm.

        Starts the generation on the entry of the maze.
        While the maze is not fully generated, the algorithm will pick a
        random direction and move there if it has not been visited yet.
        When the algorithm gets to a dead-end, it looks from left to right and
        top to bottom of the maze until it finds a visited cell that has
        neighbours which have not been visited yet.
        If it gets to the bottom-right corner of the maze while looking for a
        cell to proceed maze generation and doesn't find any, then it means
        all the cells have been visited, therefore the maze has been fully
        generated, with all cells accessible (for the sole exception of the 42
        pattern cells).
        """
        from display.display import Display

        self.start.visited = True
        cell: 'Maze.Cell' = self.start

        while True:
            if self.directions(cell):
                direction: str = rand.choice(self.directions(cell))
                cell = self.move(cell, direction)
                cell.visited = True

            print('\033[H')
            print('Maze generation algorithm: Hunt-and-kill')
            print(
                Display.print_maze(self, []),
                end='',
                flush=True
            )
            time.sleep(0.01)

            if not self.directions(cell):
                found: bool = False
                for y in range(self.height):
                    for x in range(self.width):
                        cell = self.grid[y][x]
                        if (
                            self.grid[y][x].visited and
                            self.directions(cell) and
                            any(not wall for wall in cell.walls.values())
                        ):
                            found = True
                            break
                    if found:
                        break

                if not found:
                    break

    # My own algorithm - imperfect maze
    def braid(self, base_algorithm: Callable[[], None]) -> None:
        """Generates an imperfect (braided) maze.

        Generates the maze with the algorithm provided. After the maze is
        fully generated, it will look for any dead end (cells with 3 walls)
        and break a wall, so that the maze has loops.
        This way of generating an imperfect maze prevents any large open areas
        and also prevents any closed-off areas. This way every single point of
        the maze is accessible (except the 42 pattern cells) and the maze can
        have more than one path from entry to exit.

        Args:
            base_algorithm (Callable[[], None]): The maze generating algorithm
            that will serve as the basis before the maze gets braided.
        """
        from display.display import Display

        base_algorithm()

        pattern: list[list[int]] = self.pattern_cells

        for y in range(self.height):
            for x in range(self.width):
                cell: 'Maze.Cell' = self.grid[y][x]

                walls = [w for w in cell.walls.values()]
                up_walls = [w for w in cell.walls.values() if w]
                if len(up_walls) != 3:
                    continue

                if (
                    not walls[0] and
                    y != self.height - 1 and
                    [x, y + 1] not in pattern
                ):
                    cell = self.move(cell, 'South')

                if (
                    not walls[1] and
                    x != 0 and
                    [x - 1, y] not in pattern
                ):
                    cell = self.move(cell, 'West')

                if (
                    not walls[2] and
                    y != 0 and
                    [x, y - 1] not in pattern
                ):
                    cell = self.move(cell, 'North')

                if (
                    not walls[3] and
                    x != self.width - 1 and
                    [x + 1, y] not in pattern
                ):
                    cell = self.move(cell, 'East')

                print('\033[H')

                print('Maze generation algorithm:', end=' ', flush=True)
                if base_algorithm == self.gen_dfs:
                    print('Depth-first search', flush=True)
                else:
                    print('Hunt-and-kill', flush=True)
                print(Display.print_maze(self, []), end='', flush=True)
                time.sleep(0.01)

    def to_hex_string(self) -> str:
        """Generates the maze output file string based on every cell's walls.

        Checks every cell in every row of the maze and generates a number
        ranging from 0 to 15 for that cell.
        After generating each number, it is converted to hexadecimal and
        appended to the string. After each row is written to the string, a
        newline character is added in order for it to have the same dimentions
        as the maze.

        Returns:
            str: The maze in a hexadecimal string format.
        """
        rows: list[str] = []

        for y in range(self.height):
            row: str = ''
            for x in range(self.width):
                cell = self.grid[y][x]

                value: int = 0
                if cell.walls['North']:
                    value |= 1
                if cell.walls['East']:
                    value |= 2
                if cell.walls['South']:
                    value |= 4
                if cell.walls['West']:
                    value |= 8

                cell.hex = hex(value)[2:].upper()
                row += cell.hex

            rows.append(row)

        return "\n".join(rows)

    def output(
        self,
        f: str,
        st: tuple[int, int],
        ext: tuple[int, int],
        path: str
    ) -> None:
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
            path (str): Maze solution path.
        """
        maze_string: str = self.to_hex_string()

        maze_string += f'\n\n{st[0]},{st[1]}'
        maze_string += f'\n{ext[0]},{ext[1]}'
        maze_string += f'\n{path}'

        with open(f, 'w') as output_file:
            output_file.write(maze_string)
