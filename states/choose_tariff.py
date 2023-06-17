from aiogram.dispatcher.filters.state import StatesGroup, State


class ChooseTariff(StatesGroup):
    price_input = State()


class Captcha(StatesGroup):
    captcha_input = State()
