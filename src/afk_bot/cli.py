import logging
import time

import pyautogui as pag
import typer

from afk_bot.utils import _greetings, _move_to_coordinates, _x_y_coordinates

logger = logging.getLogger(
    name=__name__,
)
logging.basicConfig(
    level=logging.INFO,
)


app = typer.Typer()


@app.command("run")
def run(
    secs: float = typer.Option(
        1.0,
        "-t",
        "--time",
        help="Interval between mouse cursor moves in seconds",
        show_default=True,
        min=1.0,
    ),
) -> int:
    """Welcome to AFK-Bot ..."""

    pag.FAILSAFE = False

    logger.info("Hope you enjoy your AFK times ...")
    logger.info(msg=_greetings())
    logger.info("To exit simply press `CTRL+C` keys ...")
    try:
        while True:
            x, y = _x_y_coordinates()
            if pag.onScreen(
                x=x,
                y=y,
            ):
                _move_to_coordinates(
                    x=x,
                    y=y,
                )
                time.sleep(secs)

                # TODO(amir): this is currently not working due to MacOS security issue
                # OSError: Error 13 - Must be run as administrator
                # https://stackoverflow.com/questions/52940429/unable-to-run-keyboard-is-pressed-on-mac
                # if keyboard.is_pressed(hotkey=_AbortKeys.Q.value) or keyboard.is_pressed(
                #     hotkey=_AbortKeys.ESC.value,
                # ):
                #     logger.info("Abort key is detected! Exiting the program ...")
                #     raise SystemExit(1)

    except KeyboardInterrupt as e:
        logger.error("Process interrupted with `CTRL+C` button ...", e)

    return 0


def main() -> None:
    """Main entry point of the bot."""
    app()
