import sys
from typing import Any
from maze import MazeGenerator as mg
from input_parser import get_flags


def main() -> None:
    try:
        flags: dict[str, Any] = get_flags(sys.argv[1])
    except Exception:
        print(f'Invalid syntax on {sys.argv[1]}')
        return

    maze = mg(flags['width'], flags['height'], flags['entry'], flags['exit'])
    maze.output(flags['output_file'])

    with open(flags['output_file'], 'r') as output_file:
        print(output_file.read())


if __name__ == '__main__':
    main()
