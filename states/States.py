from aiogram.dispatcher.filters.state import StatesGroup, State


class Form(StatesGroup):
    getPoll = State()
    addPoll = State()