from typing import List
from colorama import Style
from .walls import Walls
from .colors import random_color
from maze import Maze


LOGO_PATTERN: list[str] = [
    '██  ██   ██████ ',
    '██  ██  ██    ██',
    '██  ██       ██ ',
    '██████     ███  ',
    '    ██    ██    ',
    '    ██   ██     ',
    '    ██  ████████',
]


def lining_walls(maze: Maze, width: int, height: int) -> List[str]:
    
    "Passes the shape of the walls of the maze into a string"

    lines: List[str] = []

    for row in maze.grid:
        for i in range(2):
            place_in_row = 0
            line = ''

            for cell in row:
                if i == 0:
                    if cell.walls['North']:
                        line += str(Walls.TOP)
                    else:
                        line += str(Walls.LEFT_AND_RIGHT)
                else:
                    if cell.walls['East'] and cell.walls['West']:
                        line += str(Walls.LEFT_AND_RIGHT)
                    else:
                        if cell.walls['West']:
                            line += str(Walls.LEFT)
                        elif cell.walls['East']:
                            line += str(Walls.RIGHT)
                        else:
                            line += str(Walls.EMPTY)

                if place_in_row == width - 1:
                    lines.append(line)

                place_in_row += 1

    bottom = ''
    for cell in maze.grid[height - 1]:
        bottom += str(Walls.BOTTOM if cell.walls['South'] else Walls.EMPTY)
    lines.append(bottom)

    return lines
    
    
def coloring_logo(
    logo_row: str,
    maze_row_chars: List[str],
    left_col: int,
    color: str,
    base_color: str,
    reset: str = Style.RESET_ALL,
) -> List[str]:
    """
    Colors only the logo stroke positions for one row.
    - logo_row: one row from LOGO_PATTERN
    - maze_row_chars: editable chars for the target maze row
    - left_col: where logo starts horizontally
    """
    for i, char in enumerate(logo_row):
        col_index = left_col + i
        if char != ' ':
            # Return to maze color after each logo pixel, otherwise the
            # remaining part of the line prints with terminal default color.
            maze_row_chars[col_index] = color + char + reset + base_color
    return maze_row_chars


def overlay(lines: List[str], logo_color: str, grid_color: str) -> list[str]:

    """Overlays the walls to include the '42' pattern inside the maze
    by breaking each line of both the maze and the pattern into chars
    to make them mutable"""
    
    maze_rows = len(lines)
    maze_cols = len(lines[0])
    logo_rows = len(LOGO_PATTERN)
    logo_cols = len(LOGO_PATTERN[0])
    top_row = (maze_rows - logo_rows) // 2
    left_col = (maze_cols - logo_cols) // 2

    for i, logo_row in enumerate(LOGO_PATTERN):
        # acessando os chars individualmente pq str nn eh mutavel
        # e associando os chars pintados ao maze_row_chars
        line_index = top_row + i
        maze_row_string = lines[line_index]
        maze_row_chars = list(maze_row_string)
        maze_row_chars = coloring_logo(
            logo_row, maze_row_chars, left_col, logo_color, grid_color
        )

        # anexando a lines a nova string
        lines[line_index] = ''.join(maze_row_chars)
        i += 1

    return lines


def print_maze(maze: Maze, width: int, height: int):
    
    """Calls lining_Walls() and overlay() to make the correct maze and put 
    the 42 pattern in the center, then prints it"""
    grid_color = random_color()
    logo_color = random_color()
    while logo_color == grid_color:
        logo_color = random_color()
    lines = lining_walls(maze, width, height)
    lines = overlay(lines, logo_color, grid_color)
    # Color full maze lines only after all positioning logic is done.
    lines = [grid_color + line + Style.RESET_ALL for line in lines]
    for line in lines:
        print(line)