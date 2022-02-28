"""Unlock bot's full potential with detailed instructions."""

from aiogram import types
from aiogram.dispatcher.filters import CommandHelp

from data.constants import HELP_MSG
from loader import dp


@dp.message_handler(CommandHelp(), state="*")
@dp.throttled(rate=3)
async def give_instructions(message: types.Message):
    """Give instructions on how to use the bot."""
    await message.answer(HELP_MSG)
