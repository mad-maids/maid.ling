"""Find empty rooms based on a single message from the user.

User will be able to provide all the input for the search of empty rooms in any
of the following ways:

- just start hour (13)
- start + end hour (13-15)
- day + start hour (monday 15 | mon 15) 
- day + start + end hour (mon 15-17) 

All of these cases are handled here.
"""

from datetime import datetime

from aiogram import types

from data.constants import NO_SUNDAY, SORRY_UNEXPECTED, WEEKDAYS
from loader import dp
from utils.get_rooms import get_empty_rooms
from utils.regex import (
    ALL_PARAMS_RE,
    DAY_AND_START_RE,
    START_AND_END_RE,
    START_ONLY_RE,
)
from utils.reply import reply
from utils.validate import validate_end, validate_start


@dp.message_handler(regexp=START_ONLY_RE)
@dp.throttled(rate=3)
async def process_start_only(message: types.Message):
    """Validate start time and send a GET request.

    Check if start time is in the range 9-22 (not including 22).
    If it is, send a GET request and get all the empty rooms available at that
    time for 1 hour. So if user provides '10', the bot will return empty rooms
    available at 10-11 time slot.
    """

    await message.answer_chat_action("typing")

    start_hour = int(message.text)

    if await validate_start(start_hour, message):
        empty_rooms = await get_empty_rooms(start_hour)

        if empty_rooms:
            await reply(message, empty_rooms)
        else:
            if datetime.today().weekday() == 6:
                await message.reply(NO_SUNDAY)
            else:
                await message.reply(SORRY_UNEXPECTED)


@dp.message_handler(regexp=START_AND_END_RE)
@dp.throttled(rate=3)
async def process_start_and_end(message: types.Message):
    """Validate both start and end time and send a GET request.

    Check if start time is in the range 9-22 (not including 22) and is lower
    than end time. End time should be in the range 9-22 (not including 9).
    If everything is valid, go ahead with the GET request and get empty rooms
    for today for that specific time slot.
    """

    await message.answer_chat_action("typing")

    start_hour, end_hour = [int(item) for item in message.text.split("-")]

    if await validate_start(start_hour, message) and await validate_end(
        start_hour, end_hour, message
    ):
        empty_rooms = await get_empty_rooms(start=start_hour, end=end_hour)

        if empty_rooms:
            await reply(message, empty_rooms)
        else:
            await message.reply(SORRY_UNEXPECTED)


@dp.message_handler(regexp=DAY_AND_START_RE)
@dp.throttled(rate=3)
async def process_day_and_start(message: types.Message):
    """Validate start time and send a GET request.

    Start time should be in range 9-22 (not including 22). If start time is
    okay, send a GET request to get empty rooms on a given weekday at that time
    for one hour.
    """

    await message.answer_chat_action("typing")

    weekday, start_hour = message.text.split()
    # pls dont judge me for this dumb implementation, i know im retarded
    weekday = WEEKDAYS[weekday[:3].lower()]
    start_hour = int(start_hour)

    if await validate_start(start_hour, message):
        empty_rooms = await get_empty_rooms(start=start_hour, weekday=weekday)

        if empty_rooms:
            await reply(message, empty_rooms)
        else:
            await message.reply(SORRY_UNEXPECTED)


@dp.message_handler(regexp=ALL_PARAMS_RE)
@dp.throttled(rate=3)
async def process_all_params(message: types.Message):
    """Validate start and end time and send a GET request.

    Same requirements as previously for start and end time. If everything is
    okay with both of them, send GET request and get empty rooms on a given
    weekday for that specific time slot.
    """

    await message.answer_chat_action("typing")

    weekday, time_range = message.text.split()
    # pls dont judge me for this dumb implementation, i know im retarded
    weekday = WEEKDAYS[weekday[:3].lower()]
    start_hour, end_hour = [int(item) for item in time_range.split("-")]

    if await validate_start(start_hour, message) and await validate_end(
        start_hour, end_hour, message
    ):
        empty_rooms = await get_empty_rooms(
            start=start_hour, end=end_hour, weekday=weekday
        )

        if empty_rooms:
            await reply(message, empty_rooms)
        else:
            await message.reply(SORRY_UNEXPECTED)
