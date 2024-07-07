from aiogram.fsm.state import State, StatesGroup

class CheckSubscribe(StatesGroup):
    is_subscribe = State()
    not_subscribe = State()