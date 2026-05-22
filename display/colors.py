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
    """Returns a random color that is not in the exclude tuple

    This function makes a list of the colors excluding every color from the
    arguments and returns a random color from that list with random.choice.
    """
    filtered_colors: list[str] = [
        color for color in COLORS if color not in exclude
    ]
    return choice(filtered_colors)
