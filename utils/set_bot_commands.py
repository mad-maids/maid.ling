from aiogram import types


async def set_default_commands(dp):
    """Set commands for the bot.

    This could have also been done directly through BotFather.
    """

    await dp.bot.set_my_commands(
        [
            types.BotCommand("find", "find empty rooms"),
            types.BotCommand("help", "how to chat with me"),
            types.BotCommand("about", "brief info about me"),
            types.BotCommand("cancel", "cancel current operation"),
        ]
    )
