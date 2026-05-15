import sys
import os
import random as rand
from typing import Any
from colorama import init, Fore
from maze import Maze
from input_parser import get_flags, verify_flags
from solution import solve
from display.display import Display
from display.colors import random_color


grid_color = random_color()


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
    display = Display()

    os.system('cls')
    print(display.print_maze(maze, path[0][1:]), flush=True)

    # Sorry Miggs, mas eu nao soube fazer isso sem dar tudo append na main :,(
    print('=== A-maze-ing ===')
    i = 0
    while True:
        try:
            choice = int(input('1. Regenerate a new maze\n'
                               '2. Show/Hide path from entry to exit\n'
                               '3. Rotate maze colors\n'
                               '4. Quit\n\n'))
            if 0 > choice or choice > 4:
                print(f'\n\n{Fore.RED} ERROR')
                print('Please select a integer value between 1 and 4\n\n')
                continue
            else:
                if choice == 1:
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
                if choice == 2:
                    os.system('clear')
                    if i % 2 == 0:
                        print(display.print_maze(maze, []), flush=True)
                    else:
                        print(display.print_maze(maze, path[0][1:]), flush=True)
                    i += 1
                if choice == 3:
                    os.system('clear')
                    display.set_colors(grid_color)
                    print(display.print_maze(maze, path[0][1:]), flush=True)
                if choice == 4:
                    quit()
        except ValueError:
                print(f'\n\n{Fore.RED} ERROR')
                print('Please select a integer value between 1 and 4\n\n')
                continue


if __name__ == '__main__':
    main()
