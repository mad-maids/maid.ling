"""Main purpose is to be used while the /find command is ongoing."""

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text

from data.constants import CANCEL_MSG
from loader import dp


@dp.message_handler(Command("cancel"), state="*")
@dp.message_handler(Text(equals="Cancel"), state="*")
@dp.throttled(rate=3)
async def reset_state(message: types.Message, state: FSMContext):
    """The function name says it all."""
    await state.finish()
    await message.answer(CANCEL_MSG, reply_markup=types.ReplyKeyboardRemove())
