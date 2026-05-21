from collections import deque

def solve(maze):
    start = maze.start

    queue = deque()
    queue.append((start, [start], ''))

    visited = set()
    visited.add((start.x, start.y))

    directions = [
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
                nx = cell.x + dx
                ny = cell.y + dy

                if (nx, ny) not in visited:
                    visited.add((nx, ny))

                    next_cell = maze.grid[ny][nx]

                    queue.append((
                        next_cell,
                        path + [next_cell],
                        turns + letter
                    ))

    return ([], '')