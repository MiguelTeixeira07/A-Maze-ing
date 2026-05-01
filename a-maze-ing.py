import sys
import os
import random as rand
from typing import Any
from maze import Maze
from input_parser import get_flags, verify_flags
from colorama import init
from solution import solve
from display.display import print_maze
from display.colors import random_color


def main() -> None:
    grid_color = random_color()
    logo_color = random_color(grid_color)
    entry_color = random_color(grid_color, logo_color)
    exit_color = random_color(grid_color, logo_color, entry_color)
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

    if flags['perfect']:
        algorithm = rand.choice([maze.gen_dfs, maze.gen_hak])
        algorithm()
    else:
        maze.gen_imperfect()
    path = solve(maze)
    maze.output(flags['output_file'], flags['entry'], flags['exit'], path[1])

    os.system('clear')
    print(print_maze(maze, path[0][1:], grid_color, logo_color, entry_color, exit_color), flush=True)
    print(path[1])


if __name__ == '__main__':
    main()
