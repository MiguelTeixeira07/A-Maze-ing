import sys
import os
import random as rand
from typing import Any
from collections.abc import Callable
from colorama import init
from maze import Maze
from utils.input_parser import get_flags, verify_flags
from utils.solution import solve
from display import Display


def main_loop(
    seed: int,
    flags: dict[str, Any],
    maze: Maze,
    path: tuple[list[Maze.Cell], str],
    printing_path: bool,
    gen_algorithm: Callable[[], None]
) -> tuple[Maze, tuple[list[Maze.Cell], str], bool, Callable[[], None]]:
    """Main program loop function.

    This is the code that will be executed on the main program loop. When this
    code stops executing, the program execution has ended and there is nothing
    more to do here. The only way to stop the program once it reaces this
    point is to either kill the process, crash it or select the option that
    closes quits the program.

    Attributes:
        flags (dict[str, Any]): Configuration file flags.
        maze (Maze): Maze object.
        path (tuple[list[Maze.Cell], str]): Maze solution path.
        printing_path (bool): Is the path being printed.
        gen_algorithm (Callable[[], None]): Current maze generation algorithm.

    Returns:
        tuple[Maze, tuple[list[Maze.Cell], str], bool, Callable[[], None]]: A
        tuple containing every variable whose values need to be used in the
        next iteration.
    """
    os.system('clear')
    print()
    print('Maze generation algorithm:', end=' ')
    if gen_algorithm == maze.gen_dfs:
        print('Depth-first search')
    else:
        print('Hunt-and-kill')
    print(
        Display.print_maze(
            maze,
            path[0][1:] if printing_path else []
        ),
        '\n\n\t    === OPTIONS ===\t\t|',
        '      === MAZE STATS ===\n',
        '1 - Regenerate a new maze\t\t|',
        f'   Solution path length: {len(path[0])}\n',
        '2 - Switch maze generation algorithm\t|',
        f'   Seed: {seed}\n',
        '3 - Show/Hide path from entry to exit\t|',
        f'   Height: {maze.height}\n',
        '4 - Rotate maze colors\t\t\t|',
        f'   Width: {maze.width}\n',
        '5 - Quit\t\t\t\t|',
        f'   Total area: {maze.height * maze.width}\n',
        sep='', flush=True
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

            gen_algorithm = getattr(
                gen_algorithm,
                '__func__',
                gen_algorithm
            ).__get__(new_maze)

            if flags['perfect']:
                gen_algorithm()
            else:
                new_maze.braid(gen_algorithm)

            maze = new_maze
            path = solve(maze)

            return maze, path, printing_path, gen_algorithm

        # Change maze generation algorithm
        case '2':
            if gen_algorithm == maze.gen_dfs:
                gen_algorithm = maze.gen_hak
            else:
                gen_algorithm = maze.gen_dfs

            return maze, path, printing_path, gen_algorithm

        # Show/Hide path from entry to exit
        case '3':
            os.system('clear')
            if printing_path:
                print(Display.print_maze(maze, []))
                printing_path = False
            else:
                print(Display.print_maze(maze, path[0][1:]))
                printing_path = True

        # Rotate maze colors
        case '4':
            os.system('clear')
            Display.set_colors(exclude=Display.colors['g_color'])
            print(Display.print_maze(maze, path[0][1:]))

        # Quit
        case '5':
            maze.output(
                flags['output_file'],
                flags['entry'],
                flags['exit'],
                path[1]
            )
            sys.exit(0)

    return maze, path, printing_path, gen_algorithm


def main() -> None:
    """Main program function

    This is the main function, this mainly initializes values important to the
    program and contains the main cycle.
    """
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
    seed = rand.randint(100000000, 999999999)
    rand.seed(seed)
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
    os.system('clear')
    algorithm: Callable[[], None] = rand.choice([maze.gen_dfs, maze.gen_hak])
    if flags['perfect']:
        algorithm()
    else:
        maze.braid(algorithm)

    path: tuple[list[Maze.Cell], str] = solve(maze)
    maze.output(
        flags['output_file'],
        flags['entry'],
        flags['exit'],
        path[1]
    )

    # User input part is in an infinite loop, program will only close when the
    # user slects option 5
    while True:
        maze, path, printing_path, algorithm = main_loop(
            seed,
            flags,
            maze,
            path,
            printing_path,
            algorithm,
        )


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception:
        sys.exit(0)
