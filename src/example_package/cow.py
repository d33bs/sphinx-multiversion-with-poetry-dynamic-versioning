"""
Example module to run cowsays in demonstration repo.
"""

import cowsay


def say(message: str) -> None:
    """
    Display a cow saying the given message.

    Args:
        message: str
            The message that the cow will say.

    Returns:
        None
    """

    cowsay.cow(message)
