from random import choice
from colorama import Fore


def random_color():
    colors = [
        Fore.RED,
        Fore.BLUE,
        Fore.CYAN,
        Fore.GREEN,
        Fore.BLACK,
        Fore.YELLOW,
        Fore.MAGENTA
    ]
    return choice(colors)
