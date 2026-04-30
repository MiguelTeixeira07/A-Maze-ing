import sys
import os
from typing import Any
from maze import Maze
from input_parser import get_flags, verify_flags
from colorama import init
from solution import solve
from display.display import print_maze


def main() -> None:
    if len(sys.argv) != 2:
        print('Invalid arguments!')
        print('Usage: "python3 a-maze-ing.py <config_file>"')
        return
    init(autoreset=True)
    try:
        flags: dict[str, Any] = get_flags(sys.argv[1])
    except Exception:
        print(f'Invalid syntax on {sys.argv[1]}')
        return
    if not verify_flags(flags):
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

    os.system('clear')
    print(print_maze(maze), flush=True)
    print(path)


if __name__ == '__main__':
    main()
