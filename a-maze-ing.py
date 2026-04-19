import sys
from maze import Maze
from input_parser import get_flags

def main() -> None:
    print(sys.argv[1])
    print(get_flags(sys.argv[1]))
    print(*(f'{k}: {v}' for k, v in get_flags(sys.argv[1]).items()), sep='\n')


if __name__ == '__main__':
    main()
