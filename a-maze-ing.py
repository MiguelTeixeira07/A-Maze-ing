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


def init_colors() -> dict[str, str]:
    colors = {}

    # Ugly code bc of fckass flake8
    colors['grid_color'] = random_color()
    colors['logo_color'] = random_color(colors['grid_color'])
    colors['entry_color'] = random_color(
        colors['grid_color'],
        colors['logo_color']
    )

    colors['exit_color'] = random_color(
        colors['grid_color'],
        colors['logo_color'],
        colors['entry_color']
    )

    colors['path_color'] = random_color(
        colors['grid_color'],
        colors['logo_color'],
        colors['entry_color'],
        colors['exit_color']
    )

    return colors


def main_loop(
        flags: dict[str, Any],
        colors: dict[str, str],
        maze: Maze,
        path: tuple[list[Maze.Cell], str],
        printing_path: bool) -> bool:

    print(
        '=== A-maze-ing ===\n',
        '1. Regenerate a new maze',
        '2. Show/Hide path from entry to exit',
        '3. Rotate maze colors',
        '4. Quit\n\n', sep='\n'
    )
    choice = int(input())

    match choice:
        case 1:
            if flags['perfect']:
                algorithm = rand.choice([maze.gen_dfs, maze.gen_hak])
                algorithm()
            else:
                maze.gen_imperfect()

            path = solve(maze)
            maze.output(
                flags['output_file'],
                flags['entry'],
                flags['exit'],
                path[1]
            )

        case 2:
            os.system('clear')
            if printing_path:
                print(
                    print_maze(maze, [], *colors.values()),
                    flush=True
                )
                printing_path = False
            else:
                print(
                    print_maze(maze, path[0][1:], *colors.values()),
                    flush=True
                )
                printing_path = True

        case 3:
            os.system('clear')
            colors['grid_color'] = random_color(*colors.values())
            print(
                print_maze(maze, path[0][1:], *colors.values()),
                flush=True
            )

        case 4:
            quit()

        case _:
            print(f'\n\n{Fore.RED} ERROR')
            print('Please select a integer value between 1 and 4\n\n')

    return printing_path


def main() -> None:
    # This part parses and checks for any errors on input
    if len(sys.argv) != 2:
        print('Invalid arguments!')
        print('Usage: "python3 a-maze-ing.py <config_file>"')
        return

    try:
        flags: dict[str, Any] = get_flags(sys.argv[1])
    except Exception:
        print(f'Invalid syntax on {sys.argv[1]}')
        return

    if not verify_flags(flags):
        print(f'Invalid syntax on {sys.argv[1]}')
        return

    # After checking, initialize everything
    init(autoreset=True)
    colors = init_colors()
    printing_path = True
    maze: Maze = Maze(
        flags['width'],
        flags['height'],
        flags['entry'],
        flags['exit']
    )

    # Generate the maze once before the first choice
    if flags['perfect']:
        algorithm = rand.choice([maze.gen_dfs, maze.gen_hak])
        algorithm()
    else:
        maze.gen_imperfect()

    path = solve(maze)
    maze.output(
        flags['output_file'],
        flags['entry'],
        flags['exit'],
        path[1]
    )

    print(
        print_maze(maze, path[0][1:], *colors.values()),
        flush=True
    )

    # User input part is in an infinite loop, program will onlyclose when the
    # user slects option 4
    while True:
        printing_path = main_loop(flags, colors, maze, path, printing_path)


if __name__ == '__main__':
    main()
