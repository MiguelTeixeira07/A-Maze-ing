from random import choice
from colorama import Fore


COLORS: list[str] = [
    Fore.RED,
    Fore.BLUE,
    Fore.CYAN,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.MAGENTA
]


def random_color(*exclude: str | None) -> str:
    filtered_colors: list[str] = [
        color for color in COLORS if color not in exclude
    ]
    return choice(filtered_colors)
