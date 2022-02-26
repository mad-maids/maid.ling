"""Just a couple of states for the /find command."""

from aiogram.dispatcher.filters.state import State, StatesGroup

class FindCommand(StatesGroup):
    weekday = State()
    start_hour = State()
    end_hour = State()
