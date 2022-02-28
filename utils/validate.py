"""Very simple functions for validation.

It got very repetitive without them.
"""

from aiogram import types

from data.constants import INVALID_END, INVALID_START


async def validate_start(start: int, message: types.Message) -> bool:
    """Return True if start hour is valid else False.

    For a start hour to be valid, it should just be in the range of 9-22 (not
    including 22). If start hour is invalid, a message will be sent as a reply
    to the original message.

    Parameters
    ----------
    start : int
        start hour provided by the user
    message : aiogram.types.Message
        a message that sent the start hour, will be used if start is invalid

    Returns
    -------
    bool
        True if valid, else False
    """

    valid = 9 <= start < 22

    if not valid:
        await message.reply(INVALID_START)

    return valid


async def validate_end(start: int, end: int, message: types.Message) -> bool:
    """Return True if end hour is valid else False.

    For an end hour to be valid, it should just be in the range of 9-22 (not
    including 9) and end value should be higher than start. If end hour is
    invalid, a message will be sent as a reply to the original message.

    Parameters
    ----------
    start : int
        start hour provided by the user
    end : int
        end hour provided by the user
    message : aiogram.types.Message
        a message that sent the start hour, will be used if start is invalid

    Returns
    -------
    bool
        True if valid, else False
    """

    valid = (9 < end <= 22) and end > start

    if not valid:
        await message.reply(INVALID_END)

    return valid
