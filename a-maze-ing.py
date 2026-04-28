import sys
from typing import Any
from maze import Maze
from input_parser import get_flags
from colorama import init
from solution import solve

from display.display import print_maze


def main() -> None:
    try:
        flags: dict[str, Any] = get_flags(sys.argv[1])
    except Exception:
        print(f'Invalid syntax on {sys.argv[1]}')
        return

    maze: Maze = Maze(
        flags['width'],
        flags['height'],
        flags['entry'],
        flags['exit']
    )
    maze.gen_dfs()
    path = solve(maze)
    maze.output(flags['output_file'], flags['entry'], flags['exit'], path)

    print_maze(maze, flags['width'], flags['height'])
    print(path)


if __name__ == '__main__':
    main()
