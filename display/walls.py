from enum import Enum


class Walls(Enum):
    """Represents the possible states to print a wall.

    Attributes:
        EMPTY: No top wall.
        TOP: Top wall.
        LEFT: Left wall only.
        RIGHT: Right wall only.
        LEFT_AND_RIGHT: Left and right wall in the same cell.
    """
    EMPTY = '     '

    TOP = '█████'

    RIGHT = '    █'

    LEFT = '█    '

    LEFT_AND_RIGHT = '█   █'

    def __str__(self) -> str:
        """Turns each value into a string

        Converts each value into a string for them to be printable instead of
        an instance.

        Returns:
            str: The value being retrieved as a string.
        """
        return str(self.value)
