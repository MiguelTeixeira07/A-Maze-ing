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

    def __init__(self, w: int, h: int, start: bool, exit: bool) -> None:
        self.width = w
        self.height = h

        self.grid = [
            [Maze.Cell() for x in range(w)]
            for y in range(h)
        ]
