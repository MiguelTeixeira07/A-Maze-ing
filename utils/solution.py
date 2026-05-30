from collections import deque
from maze import Maze


def solve(maze: Maze) -> tuple[list[Maze.Cell], str]:
    """Solves the maze.

    The maze is solved using a breadth-first search algorithm.
    This means that for every cell that has more than one possible path, the
    algorithm will store this interception in a queue and go to the one that
    has been on the queue for the longest, for every interception this process
    is repeated until the exit is found. This way the shortest path to the
    exit will be found every single time.

    Args:
        maze (Maze): Maze object.

    Returns:
        tuple[list[Maze.Cell], str]: a tuple that contains the list of cells
        that are on the path to the exit and the string that will later go to
        the output file.
    """
    start: Maze.Cell = maze.start

    queue: deque[tuple[Maze.Cell, list[Maze.Cell], str]] = deque()
    visited: set[tuple[int, int]] = set()

    queue.append((start, [start], ''))
    visited.add((start.x, start.y))

    directions: list[tuple[str, int, int, str]] = [
        ('North', 0, -1, 'N'),
        ('East', 1, 0, 'E'),
        ('South', 0, 1, 'S'),
        ('West', -1, 0, 'W')
    ]

    while queue:
        cell, path, turns = queue.popleft()

        if cell.exit:
            return (path, turns)

        for wall, dx, dy, letter in directions:
            if not cell.walls[wall]:
                nx: int = cell.x + dx
                ny: int = cell.y + dy

                if (nx, ny) not in visited:
                    visited.add((nx, ny))

                    next_cell: Maze.Cell = maze.grid[ny][nx]

                    queue.append((
                        next_cell,
                        path + [next_cell],
                        turns + letter
                    ))

    return ([], '')
