from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def tariff_price_kb_func():
    tariff_price_keyboard = InlineKeyboardMarkup()
    tariff_price_1_btn = InlineKeyboardButton(text='до 100 грн', callback_data=f'tariff_price:lte_100')
    tariff_price_2_btn = InlineKeyboardButton(text='від 101 до 250 грн', callback_data=f'tariff_price:in_101_250')
    tariff_price_3_btn = InlineKeyboardButton(text='від 251 грн', callback_data=f'tariff_price:gte_251')
    back_btn = InlineKeyboardButton(text='< Назад', callback_data=f'back:')
    tariff_price_keyboard.add(tariff_price_1_btn, tariff_price_2_btn, tariff_price_3_btn)
    tariff_price_keyboard.add(back_btn)
    return tariff_price_keyboard


async def internet_input_kb_func():
    internet_input_keyboard = InlineKeyboardMarkup()
    internet_input_1_btn = InlineKeyboardButton(text='до 7 ГБ', callback_data=f'tariff_internet:lte_7')
    internet_input_2_btn = InlineKeyboardButton(text='від 7 до 30 ГБ', callback_data=f'tariff_internet:in_7_30')
    internet_input_3_btn = InlineKeyboardButton(text='від 30 до Безліміт', callback_data=f'tariff_internet:in_30_999999')
    back_btn = InlineKeyboardButton(text='< Назад', callback_data=f'back:')
    internet_input_keyboard.add(internet_input_1_btn, internet_input_2_btn, internet_input_3_btn)
    internet_input_keyboard.add(back_btn)
    return internet_input_keyboard


async def time_input_kb_func():
    time_input_keyboard = InlineKeyboardMarkup()
    time_input_1_btn = InlineKeyboardButton(text='до 300 хв', callback_data=f'tariff_time:lte_300')
    time_input_2_btn = InlineKeyboardButton(text='від 301 до 1500 хв', callback_data=f'tariff_time:in_301_1500')
    time_input_3_btn = InlineKeyboardButton(text='від 1501 до Безліміт', callback_data=f'tariff_time:minutes=in_1501_100000005')
    back_btn = InlineKeyboardButton(text='< Назад', callback_data=f'back:')
    time_input_keyboard.add(time_input_1_btn, time_input_2_btn, time_input_3_btn)
    time_input_keyboard.add(back_btn)
    return time_input_keyboard


async def connect_type_input_kb_func():
    connect_type_input_keyboard = InlineKeyboardMarkup()
    connect_type_input_1_btn = InlineKeyboardButton(text='Контракт', callback_data=f'tariff_connect_type:contractqwerty')
    connect_type_input_2_btn = InlineKeyboardButton(text='Передоплата', callback_data=f'tariff_connect_type:predoplata')
    back_btn = InlineKeyboardButton(text='< Назад', callback_data=f'back:')
    connect_type_input_keyboard.add(connect_type_input_1_btn, connect_type_input_2_btn)
    connect_type_input_keyboard.add(back_btn)
    return connect_type_input_keyboard


async def loyalty_input_kb_func():
    loyalty_input_keyboard = InlineKeyboardMarkup()
    loyalty_input_1_btn = InlineKeyboardButton(text='PLATINUM Клуб', callback_data=f'tariff_loyalty:platinum-klub')
    loyalty_input_2_btn = InlineKeyboardButton(text='Знижки для студентів', callback_data=f'tariff_loyalty:znizhki-dlya-studentiv')
    back_btn = InlineKeyboardButton(text='< Назад', callback_data=f'back:')
    loyalty_input_keyboard.add(loyalty_input_1_btn, loyalty_input_2_btn)
    loyalty_input_keyboard.add(back_btn)
    return loyalty_input_keyboard
