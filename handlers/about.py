"""Find out more about the bot here."""

from aiogram import types
from aiogram.dispatcher.filters import Command

from data.constants import ABOUT_MSG
from loader import dp


@dp.message_handler(Command("about"), state="*")
@dp.throttled(rate=3)
async def introduce_self(message: types.Message):
    """Give a brief introduction about the bot."""
    await message.answer(ABOUT_MSG)
