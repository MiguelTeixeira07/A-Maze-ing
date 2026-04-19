from typing import Optional as Opt


class Maze:
    class Cell:
        def __init__(self, start=False, exit=False) -> None:
            self.start = start
            self.exit = exit

            self.walls = {
                'North': False,
                'East': False,
                'South': False,
                'West': False
            }

    def __init__(self, w: int, h: int, st: list[int], ext: list[int]) -> None:
        self.width = w
        self.height = h
        self.grid = []

        for y in range(h):
            self.grid.append([])
            for x in range(w):
                start = [x, y] == st
                exit = [x, y] == ext

                self.grid[y].append(Maze.Cell(start, exit))

    def randomize(self) -> None:
        pass
