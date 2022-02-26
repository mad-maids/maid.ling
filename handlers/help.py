"""Unlock bot's full potential with detailed instructions."""

from aiogram import types
from aiogram.dispatcher.filters import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp(), state="*")
@dp.throttled(rate=3)
async def give_instructions(message: types.Message):
    """Give instructions on how to use the bot."""
    await message.answer(
        "<b>INSTRUCTIONS</b>\n"
        "There are two ways I process requests:\n"
        "- Taking input from you step by step with the <b>/find</b> command.\n"
        "- The more convenient way - taking all needed input from a single "
        "message (or as I like to call this: <i>single message mode</i>).\n\n"
        "Since both of these methods are very similar in nature, I'll explain "
        "the second one in detail (first is straightforward).\n\n"
        "All you need to tell me are 3 things:\n"
        "1. <i>start hour</i> - from what hour should the room be free\n"
        "2. <i>end hour</i> - till what hour <b>(not including this hour)</b> "
        "should the room be free\n"
        "3. <i>weekday</i> - the day of the week that you are interested in\n"
        "\n<b>EXAMPLE</b>\n"
        "Let's say you need an empty room for Monday from 12 till 14 (for 2 "
        "hours).\nAll you have to do is type: <code>monday 12-14</code> and I "
        "will find all empty rooms avaialable.\n"
        "\n<b>SOME INFO IS OPTIONAL</b>\n"
        "If you're using the <i>single message mode</i>, to save time, you can "
        "omit some details."
        "\n - If you need a room for only one hour, let's say on Tuesday from "
        "13-14, you can just text: <code>tuesday 12</code>"
        "\n - You can even save more time by providing the abbreviation for a "
        "given weekday: <code>tue 12</code>"
        "\n - And if it just so happens that you are looking for an empty room "
        "for today, you are in luck, you can omit the weekday altogether: "
        "<code>17-19</code>"
        "\n - Finally, if you need a room today for just one hour, u can give "
        "the simplest request: <code>17</code>\n\n"
        "<b>NOTES</b>\n"
        "- Casing is ignored when typing weekday: MONDAY is same as monday and "
        "even mOnDAY (if you type like this, you should go to a therapist).\n"
        "- Valid values for start and end hour are only integer values, so "
        "I won't understand anything like 17:30 or 17.5.\n"
        "- Additionally, since university open at 9 and closes at around 22, "
        "start can't be lower than 9 or higher than 21. Similarly, end cannot "
        "be lower than 10 or higher than 22.\n"
        "- You can't omit details if you are using <b>/find</b> command."
    )
