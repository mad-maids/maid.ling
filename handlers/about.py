"""Find out more about the bot here."""

from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command("about"), state="*")
@dp.throttled(rate=3)
async def introduce_self(message: types.Message):
    """Give a brief introduction about the bot."""
    await message.answer(
        "I'm <b>Qiao Ling</b>, your personal room finder assistant.\n"
        "With my help, you can find empty rooms in an instant.\n"
        "Say goodbye to wasting time on timetable page going through each room "
        "on the dropdown menu!\n\n"
        "<b>FUN FACT</b>\nI'm actually Chinese and from a <i>Donghua</i> called "
        "<a href='https://myanimelist.net/anime/44074/Shiguang_Dailiren'>Link "
        "Click</a> (not sponsored)."
    )
