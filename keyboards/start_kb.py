from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def choose_order_kb_func():
    choose_order_keyboard = InlineKeyboardMarkup()
    choose_tariff_btn = InlineKeyboardButton(text='🔍 Обрати Тариф', callback_data=f'choose_order:')
    support_btn = InlineKeyboardButton(text='👨‍🔧 Тех Підтримка', url='https://t.me/nomiss7')
    close_btn = InlineKeyboardButton(text='🗑 Закрити', callback_data=f'close:')
    choose_order_keyboard.add(choose_tariff_btn)
    choose_order_keyboard.add(support_btn)
    choose_order_keyboard.add(close_btn)
    return choose_order_keyboard


async def new_captcha_kb_func():
    new_captcha_btn = InlineKeyboardButton(text='➕ Запросити нову капчу',
                                           callback_data=f'new_captcha:')
    new_captcha_keyboard = InlineKeyboardMarkup().add(new_captcha_btn)

    return new_captcha_keyboard
