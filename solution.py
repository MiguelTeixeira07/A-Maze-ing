from maze import Maze


def solve(maze: Maze) -> tuple[list[Maze.Cell], str]:
    def flood_fill(
        cell: Maze.Cell,
        path: list[Maze.Cell],
        turns: str
    ) -> tuple[list[Maze.Cell], str]:

        if cell.exit:
            return (path, turns)

        cell.sv = True

        if not cell.walls['North'] and not maze.grid[cell.y - 1][cell.x].sv:
            result = flood_fill(
                maze.grid[cell.y - 1][cell.x],
                [*path, cell],
                turns + 'N'
            )
            if result[0] and result[1]:
                return result

        if not cell.walls['East'] and not maze.grid[cell.y][cell.x + 1].sv:
            result = flood_fill(
                maze.grid[cell.y][cell.x + 1],
                [*path, cell],
                turns + 'E'
            )
            if result[0] and result[1]:
                return result

        if not cell.walls['South'] and not maze.grid[cell.y + 1][cell.x].sv:
            result = flood_fill(
                maze.grid[cell.y + 1][cell.x],
                [*path, cell],
                turns + 'S'
            )
            if result[0] and result[1]:
                return result

        if not cell.walls['West'] and not maze.grid[cell.y][cell.x - 1].sv:
            result = flood_fill(
                maze.grid[cell.y][cell.x - 1],
                [*path, cell],
                turns + 'W'
            )
            if result[0] and result[1]:
                return result

        return ([], '')

    return flood_fill(maze.start, [], '')
