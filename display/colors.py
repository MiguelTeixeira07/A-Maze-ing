from random import choice
from colorama import Fore


def random_color(*exclude) -> str:
    colors = [
        Fore.RED,
        Fore.BLUE,
        Fore.CYAN,
        Fore.GREEN,
        Fore.BLACK,
        Fore.YELLOW,
        Fore.MAGENTA
    ]

    filtered_colors = [color for color in colors if color not in exclude]
    return choice(filtered_colors)
