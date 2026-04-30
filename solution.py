from maze import Maze


def solve(maze: Maze) -> str:
    def flood_fill(cell: Maze.Cell, turns: str) -> str:
        if cell.exit:
            return turns
        
        cell.sv = True

        if not cell.walls['North'] and not maze.grid[cell.y - 1][cell.x].sv:
            result = flood_fill(maze.grid[cell.y - 1][cell.x], turns + 'N')
            if result:
                return result

        if not cell.walls['East'] and not maze.grid[cell.y][cell.x + 1].sv:
            result = flood_fill(maze.grid[cell.y][cell.x + 1], turns + 'E')
            if result:
                return result

        if not cell.walls['South'] and not maze.grid[cell.y + 1][cell.x].sv:
            result = flood_fill(maze.grid[cell.y + 1][cell.x], turns + 'S')
            if result:
                return result

        if not cell.walls['West'] and not maze.grid[cell.y][cell.x - 1].sv:
            result = flood_fill(maze.grid[cell.y][cell.x - 1], turns + 'W')
            if result:
                return result

        return ''

    return flood_fill(maze.start, '')
