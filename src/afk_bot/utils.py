import random
from enum import Enum, IntEnum
from typing import List, Optional, Tuple

import pyautogui as pag


class _X(IntEnum):
    """Contains min/max for X coordinate."""

    MIN = 1
    MAX = pag.size().width


class _Y(IntEnum):
    """Contains min/max for Y coordinate."""

    MIN = 1
    MAX = pag.size().height


class _AbortKeys(Enum):
    """Abort keys to exit the program."""

    Q = "q"
    ESC = "esc"

    @classmethod
    def keys(cls) -> List[str]:
        """Returns a list of abort keys as string.

        Returns
        -------
        List[str]
        """
        return [c.value for c in cls]


def _x_y_coordinates() -> Tuple[int, int]:
    """Returns a random (x,y) coordinates.

    Returns
    -------
    Tuple[int, int]
    """
    x = random.randint(
        a=_X.MIN,
        b=_X.MAX,
    )
    y = random.randint(
        a=_Y.MIN,
        b=_Y.MAX,
    )

    return x, y


def _move_to_coordinates(
    x: int,
    y: int,
    duration: Optional[float] = 0.5,
) -> None:
    """Moves the cursor to (x,y) coordinates.

    Parameters
    ----------
    x : int
        X coordinate

    y : int
        Y coordinate

    Returns
    -------
    None
    """
    pag.moveTo(
        x=x,
        y=y,
        duration=duration,
    )

    return None


def _greetings() -> str:
    """Returns the `AFK-Bot` greetings logo.

    Returns
    -------
    str
    """
    return """\n
 █████╗ ███████╗██╗  ██╗     ██████╗  ██████╗ ████████╗
██╔══██╗██╔════╝██║ ██╔╝     ██╔══██╗██╔═══██╗╚══██╔══╝
███████║█████╗  █████╔╝█████╗██████╔╝██║   ██║   ██║
██╔══██║██╔══╝  ██╔═██╗╚════╝██╔══██╗██║   ██║   ██║
██║  ██║██║     ██║  ██╗     ██████╔╝╚██████╔╝   ██║
╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝     ╚═════╝  ╚═════╝    ╚═╝\n
    """
