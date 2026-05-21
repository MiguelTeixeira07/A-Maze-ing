import sys
import os
import random as rand
from typing import Any
from collections.abc import Callable
from colorama import init
from mazegen.maze import Maze
from input_parser import get_flags, verify_flags
from solution import solve
from display import Display


def main_loop(
    flags: dict[str, Any],
    maze: Maze,
    path: tuple[list[Maze.Cell], str],
    printing_path: bool
) -> tuple[Maze, tuple[list[Maze.Cell], str], bool]:
    os.system('clear')
    print(
        Display.print_maze(
            maze,
            path[0][1:] if printing_path else []
        ),
        '\n=== A-maze-ing ===\n',
        '1. Regenerate a new maze',
        '2. Show/Hide path from entry to exit',
        '3. Rotate maze colors',
        '4. Quit\n\n', sep='\n'
    )
    choice: str = input()

    match choice:
        # Regenerate a new maze
        case '1':
            new_maze: Maze = Maze(
                flags['width'],
                flags['height'],
                flags['entry'],
                flags['exit']
            )

            if flags['perfect']:
                algorithm: Callable[[], None] = rand.choice(
                    [new_maze.gen_dfs, new_maze.gen_hak]
                )
                algorithm()
            else:
                new_maze.gen_imperfect()

            maze = new_maze
            path = solve(maze)

            return maze, path, printing_path

        # Show/Hide path from entry to exit
        case '2':
            os.system('clear')
            if printing_path:
                print(Display.print_maze(maze, []))
                printing_path = False
            else:
                print(Display.print_maze(maze, path[0][1:]))
                printing_path = True

        # Rotate maze colors
        case '3':
            os.system('clear')
            Display.set_colors(exclude=Display.colors['g_color'])
            print(Display.print_maze(maze, path[0][1:]))

        # Quit
        case '4':
            maze.output(
                flags['output_file'],
                flags['entry'],
                flags['exit'],
                path[1]
            )
            quit()

    return maze, path, printing_path


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
    Display.set_colors()
    maze: Maze = Maze(
        flags['width'],
        flags['height'],
        flags['entry'],
        flags['exit']
    )
    printing_path: bool = True

    # Generate the maze once before the first choice
    if flags['perfect']:
        algorithm: Callable[[], None] = rand.choice(
            [maze.gen_dfs, maze.gen_hak]
        )
        algorithm()
    else:
        maze.gen_imperfect()

    path: tuple[list[Maze.Cell], str] = solve(maze)
    if path[1] == '':
        print('Maze entry/exit is one of the pattern cells')
        return
    maze.output(
        flags['output_file'],
        flags['entry'],
        flags['exit'],
        path[1]
    )

    # User input part is in an infinite loop, program will onlyclose when the
    # user slects option 4
    while True:
        maze, path, printing_path = main_loop(
            flags,
            maze,
            path,
            printing_path
        )


if __name__ == '__main__':
    main()
