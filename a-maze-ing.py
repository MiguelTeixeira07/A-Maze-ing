import sys
from typing import Any
from maze import Maze as mg
from input_parser import get_flags
from display.display import print_maze


def main() -> None:
    try:
        flags: dict[str, Any] = get_flags(sys.argv[1])
    except Exception:
        print(f'Invalid syntax on {sys.argv[1]}')
        return

    maze: mg = mg(flags['width'], flags['height'], flags['entry'], flags['exit'])
    path = 'SSSSSSSSSSSSSSSSSSSEEEEEEEEEEEEEE'
    maze.gen_dfs()
    maze.output(flags['output_file'], flags['entry'], flags['exit'], path)

    print_maze(maze, flags['width'], flags['height'])


if __name__ == '__main__':
    main()
