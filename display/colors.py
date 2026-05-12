from random import choice
from colorama import Fore


COLORS = [
    Fore.RED,
    Fore.BLUE,
    Fore.CYAN,
    Fore.GREEN,
    Fore.BLACK,
    Fore.YELLOW,
    Fore.MAGENTA
]

def random_color(*exclude: str) -> str:

    filtered_colors = [color for color in COLORS if color not in exclude]
    return choice(filtered_colors)
