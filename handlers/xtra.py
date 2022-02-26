"""Extra stuff, hidden references to Link Click."""

from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.utils.emoji import emojize

from loader import dp
from utils.regex import JOJO_RE


@dp.message_handler(Text(contains="old witch", ignore_case=True))
async def how_dare_you(message: types.Message):
    """Indespicable."""
    await message.reply(f"WHAT? AN OLD WITCH? {emojize(':rage:')}")


@dp.message_handler(regexp=JOJO_RE)
async def thats_not_my_nickname(message: types.Message):
    """Damn it, why can't they get it right?"""
    await message.reply("Not JO JO! It's Qiao Qiao!")


@dp.message_handler()
async def nudge(message: types.Message):
    """Let the user know that they can get instructions via /help."""
    await message.reply(
        "If you're confused about anything, feel free to get <b>/help</b>."
    )
