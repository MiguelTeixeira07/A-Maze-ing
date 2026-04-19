from typing import Optional as Opt


class Maze:
    class Cell:
        def __init__(self, start=False, exit=False) -> None:
            self.start = start
            self.exit = exit

            self.walls = {
                'North': True,
                'East': True,
                'South': True,
                'West': True
            }

            self.visited = False

    def __init__(self, w: int, h: int, start: tuple, exit: tuple) -> None:
        self.width = w
        self.height = h

        self.grid = []
        for y in range(h):
            self.grid.append([])
            for x in range(w):
                is_start = start[0] == x and start[1] == y
                is_exit = exit[0] == x and exit[1] == y
                self.grid[y][x] = Maze.Cell(is_start, is_exit)
