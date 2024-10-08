"""
Example module to run cowsays in demonstration repo.
"""

import cowsay


def say(message: str) -> None:
    """
    Display a cow saying the given message.
    It's pretty awesome.

    Args:
        message: str
            The message that the cow will say.

    Returns:
        None
    """

    cowsay.cow(message)

def move() -> None:
    """
    Print a statement about the cow moving.

    Returns:
        None
    """
    print("The cow moved.")
