import sys
import os
import random as rand
from typing import Any
from colorama import init, Fore
from maze import Maze
from input_parser import get_flags, verify_flags
from solution import solve
from display.display import print_maze
from display.colors import random_color


grid_color = random_color()
logo_color = random_color(grid_color)
entry_color = random_color(grid_color, logo_color)
exit_color = random_color(grid_color, logo_color, entry_color)


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

    # Sorry Miggs, mas eu nao soube fazer isso sem dar tudo append na main :,(
    print('=== A-maze-ing ===')
    while True:
        try:
            choice = int(input('1. Regenerate a new maze\n'
                    '2. Show/Hide path from entry to exit\n'
                    '3. Rotate maze colors\n'
                    '4. Quit\n'))
            if 0 > choice or choice > 4:
                print(f'\n\n{Fore.RED} ERROR')
                print('Please select a integer value between 1 and 4\n\n')
                continue
            else:
                if choice == 1:
                    main()
                if choice == 2:
                    pass
                if choice == 3:
                    os.system('clear')
                    new_grid_color = random_color(grid_color, logo_color, entry_color, exit_color)
                    print(print_maze(maze, path[0][1:], new_grid_color, logo_color, entry_color, exit_color), flush=True)
                if choice == 4:
                    quit()
        except ValueError:
                print(f'\n\n{Fore.RED} ERROR')
                print('Please select a integer value between 1 and 4\n\n')
                continue


if __name__ == '__main__':
    main()
