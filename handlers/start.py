"""Basic handlert for start. Encourage user to check out help."""

from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from data.constants import START_MSG
from loader import dp


@dp.message_handler(CommandStart(), state="*")
@dp.throttled(rate=3)
async def greet_user(message: types.Message):
    """Greet user on start."""
    await message.answer(START_MSG)
