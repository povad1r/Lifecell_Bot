from aiogram.dispatcher.filters.state import StatesGroup, State


class ChooseTariff(StatesGroup):
    price_input = State()
    internet_input = State()
    time_input = State()
    connect_type_input = State()
    loyalty_input = State()


class Captcha(StatesGroup):
    captcha_input = State()
