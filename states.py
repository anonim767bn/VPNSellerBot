from aiogram.fsm.state import State, StatesGroup


class Agreement(StatesGroup):
    waiting_for_agreement = State()
    