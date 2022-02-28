"""A simple function to avoid repetitiveness."""

from typing import List

from aiogram import types

from utils.formatter import format_dict
from utils.process_rooms import process_rooms


async def reply(message: types.Message, rooms: List[str]):
    """Prepare and send back a reply to the user.

    This is used a lot in single_find.py

    Parameters
    ----------
    message : types.Message
        a message to which the bot should reply with the processed empty rooms
    rooms : List[str]
        a list of empty rooms (not ready to send)
    """

    processed_rooms = process_rooms(rooms)
    text = format_dict(processed_rooms)
    await message.reply(text)
