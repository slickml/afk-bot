import pyautogui as pag
from assertpy import assert_that

from afk_bot.utils import (
    _X,
    _Y,
    _AbortKeys,
    _greetings,
    _move_to_coordinates,
    _x_y_coordinates,
)


def test_x_y_coordinates() -> None:
    """Validates the x-y coordinates generation."""
    x, y = _x_y_coordinates()

    assert_that(x).is_instance_of(int)
    assert_that(y).is_instance_of(int)
    assert_that(x).is_between(_X.MIN, _X.MAX)
    assert_that(y).is_between(_Y.MIN, _Y.MAX)


def test_move_to_coordinates() -> None:
    """Validates the cooridinates after the move."""
    x, y = _x_y_coordinates()
    if pag.onScreen(x, y):
        _move_to_coordinates(
            x=x,
            y=y,
        )
    current_coordinates = pag.position()

    assert_that(current_coordinates.x).is_equal_to(x)
    assert_that(current_coordinates.y).is_equal_to(y)


def test_abort_keys() -> None:
    """Validates the abort keys."""

    assert_that(_AbortKeys.keys()).is_equal_to(["q", "esc"])


def test_greetings() -> None:
    """Validates the greetings message."""
    s = _greetings()

    assert_that(s).is_instance_of(str)
