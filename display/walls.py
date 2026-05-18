from enum import Enum
from typing import Literal


class Walls(Enum):
    EMPTY: Literal["     "] = "     "

    TOP: Literal["█████"] = "█████"

    RIGHT: Literal["    █"] = "    █"

    LEFT: Literal["█    "] = "█    "

    LEFT_AND_RIGHT: Literal["█   █"] = "█   █"

    def __str__(self) -> str:
        return str(self.value)
