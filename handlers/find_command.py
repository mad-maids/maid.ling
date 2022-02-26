"""Another way to find empty rooms using a command.

This is a very basic 3 step process of taking input from the user and making a
final GET request at the end.
1. ask to input weekday
2. ask to input start
3. ask to input end
"""


from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.states import FindCommand
from utils.formatter import format_dict
from utils.get_rooms import get_empty_rooms
from utils.process_rooms import process_rooms
from utils.regex import START_ONLY_RE, WEEKDAYS_RE
from utils.validate import validate_end, validate_start

START_HOURS = [str(n) for n in range(9, 22)]


@dp.message_handler(Command("find"))
@dp.throttled(rate=3)
async def send_weekday_keyboard(message: types.Message):
    """Ask user to pick a weekday from a Reply keyboard."""
    await FindCommand.weekday.set()
    await message.answer_chat_action(action="typing")

    week_days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ]

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*week_days)
    keyboard.add("Cancel")

    await message.answer(
        "Please choose the weekday you are interested in.",
        reply_markup=keyboard,
    )


@dp.message_handler(regexp=WEEKDAYS_RE, state=FindCommand.weekday)
async def send_start_keyboard(message: types.Message, state: FSMContext):
    """Ask user to pick a start hour from a Reply keyboard."""
    await FindCommand.start_hour.set()
    await message.answer_chat_action(action="typing")
    await state.update_data(weekday=message.text)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*START_HOURS)
    keyboard.add("Cancel")

    await message.answer("Please pick a start hour.", reply_markup=keyboard)


@dp.message_handler(regexp=START_ONLY_RE, state=FindCommand.start_hour)
async def send_end_keyboard(message: types.Message, state: FSMContext):
    """Ask user to pick an end hour from a Reply keyboard."""
    start_hour = int(message.text)

    if not await validate_start(start_hour, message):
        return

    await FindCommand.end_hour.set()
    await message.answer_chat_action(action="typing")
    await state.update_data(start=message.text)

    end_hours = START_HOURS[START_HOURS.index(str(start_hour)) + 1 :]
    end_hours.append("22")

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*end_hours)
    keyboard.add("Cancel")

    await message.answer("Please pick an end hour.", reply_markup=keyboard)


@dp.message_handler(regexp=START_ONLY_RE, state=FindCommand.end_hour)
async def process_find_request(message: types.Message, state: FSMContext):
    """Find empty rooms with all the given user input."""
    req_data = await state.get_data()
    start_hour = int(req_data["start"])
    end_hour = int(message.text)

    if not await validate_end(start_hour, end_hour, message):
        return

    weekday = req_data["weekday"]
    await message.answer_chat_action(action="typing")

    empty_rooms = await get_empty_rooms(
        start=start_hour, end=end_hour, weekday=weekday
    )

    if empty_rooms:
        processed_rooms = process_rooms(empty_rooms)
        text = format_dict(processed_rooms)
        await message.answer(text, reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.reply(
            "Something went wrong, gomennasai.",
            reply_markup=types.ReplyKeyboardRemove(),
        )

    await state.finish()
