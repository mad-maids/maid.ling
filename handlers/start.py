"""Basic handlert for start. Encourage user to check out help."""

from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from loader import dp


@dp.message_handler(CommandStart(), state="*")
@dp.throttled(rate=3)
async def greet_user(message: types.Message):
    """Greet user on start."""
    await message.answer(
        "Hello there, you can call me <b>Qiao Qiao</b>. If you need an empty "
        "room at WIUT for whatever reason, I can help you. For more info, check "
        "out <b>/help</b> or <b>/about</b>."
    )
