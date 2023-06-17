from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from create_bot import dp, db, bot
from keyboards import start_kb
from keyboards.tariff_kb import tariff_price_kb_func, internet_input_kb_func, time_input_kb_func, \
    connect_type_input_kb_func, loyalty_input_kb_func
from utils.scrape_tariffs import scrape_tariffs_func
from states import choose_tariff


async def back(call: CallbackQuery, state: FSMContext):
    if await choose_tariff.ChooseTariff.previous():
        await tariff_callback_messages(call=call, current_state=await state.get_state())
    else:
        await state.finish()

        try:
            await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        except:
            pass

        photo = open('static/lifecell.gif', 'rb')
        await bot.send_animation(chat_id=call.message.chat.id,
                                 animation=photo,
                                 caption=f'<b>👋 Привіт!\n➖➖➖➖➖➖➖➖➖➖➖\n'
                                         f'📈 Цей бот допоможе тобі обрати вигідний тариф компанії «Lifecell»</b>',
                                 reply_markup=await start_kb.choose_order_kb_func(),
                                 parse_mode='HTML')
    await call.answer('Ви повернулися назад!')


async def tariff_order(call: CallbackQuery, state: FSMContext):
    try:
        await bot.delete_message(chat_id=call,
                                 message_id=call.message.message_id)
    except:
        pass
    await choose_tariff.ChooseTariff.price_input.set()
    await tariff_callback_messages(call=call, current_state=await state.get_state())


async def input_tariff_price(call: CallbackQuery, state: FSMContext):
    button, price = call.data.split(':')
    async with state.proxy() as data:
        data['tariff_price'] = price
    await choose_tariff.ChooseTariff.internet_input.set()
    await tariff_callback_messages(call=call, current_state=await state.get_state())


async def input_tariff_internet(call: CallbackQuery, state: FSMContext):
    button, internet = call.data.split(':')
    async with state.proxy() as data:
        data['tariff_internet'] = internet
    await choose_tariff.ChooseTariff.time_input.set()
    await tariff_callback_messages(call=call, current_state=await state.get_state())


async def input_tariff_time(call: CallbackQuery, state: FSMContext):
    button, time = call.data.split(':')
    async with state.proxy() as data:
        data['tariff_time'] = time
    await choose_tariff.ChooseTariff.connect_type_input.set()
    await tariff_callback_messages(call=call, current_state=await state.get_state())


async def input_tariff_connect_type(call: CallbackQuery, state: FSMContext):
    button, connect_type = call.data.split(':')
    async with state.proxy() as data:
        data['tariff_connect_type'] = connect_type
    await choose_tariff.ChooseTariff.loyalty_input.set()
    await tariff_callback_messages(call=call, current_state=await state.get_state())


async def input_tariff_loyalty(call: CallbackQuery, state: FSMContext):
    button, loyalty = call.data.split(':')
    async with state.proxy() as data:
        data['tariff_loyalty'] = loyalty

        tariffs = await scrape_tariffs_func(price=data['tariff_price'],
                                            internet=data['tariff_internet'],
                                            time=data['tariff_time'],
                                            connect_type=data['tariff_connect_type'],
                                            loyalty_input=data['tariff_loyalty'])
        await bot.send_message(chat_id=call.message.chat.id,
                               text=f'{tariffs}',
                               parse_mode='HTML')
        try:
            await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        except:
            pass
        await state.finish()


async def tariff_callback_messages(call, current_state):
    if current_state == f'ChooseTariff:price_input':
        await call.message.edit_caption(caption=f'<b>💸 Оберіть бажану ціну тарифу:</b>',
                                        reply_markup=await tariff_price_kb_func(),
                                        parse_mode='HTML')
    elif current_state == f'ChooseTariff:internet_input':
        await call.message.edit_caption(caption=f'<b>📊 Оберіть бажаний інтернет ліміт:</b>',
                                     reply_markup=await internet_input_kb_func(),
                                     parse_mode='HTML')
    elif current_state == f'ChooseTariff:time_input':
        await call.message.edit_caption(caption=f'<b>🕔 Оберіть бажаний ліміт по часу:</b>',
                                     reply_markup=await time_input_kb_func(),
                                     parse_mode='HTML')
    elif current_state == f'ChooseTariff:connect_type_input':
        await call.message.edit_caption(caption=f'<b>📲 Оберіть бажаний тип підключення:</b>',
                                     reply_markup=await connect_type_input_kb_func(),
                                     parse_mode='HTML')
    elif current_state == f'ChooseTariff:loyalty_input':
        await call.message.edit_caption(caption=f'<b>🚦 Оберіть бажану лояльність:</b>',
                                     reply_markup=await loyalty_input_kb_func(),
                                     parse_mode='HTML')


def register_handlers_tariff(dp: Dispatcher):
    dp.register_callback_query_handler(back, text='back:', state='*')
    dp.register_callback_query_handler(tariff_order, text='choose_order:', state='*')
    dp.register_callback_query_handler(input_tariff_price, state=choose_tariff.ChooseTariff.price_input)
    dp.register_callback_query_handler(input_tariff_internet, state=choose_tariff.ChooseTariff.internet_input)
    dp.register_callback_query_handler(input_tariff_time, state=choose_tariff.ChooseTariff.time_input)
    dp.register_callback_query_handler(input_tariff_connect_type, state=choose_tariff.ChooseTariff.connect_type_input)
    dp.register_callback_query_handler(input_tariff_loyalty, state=choose_tariff.ChooseTariff.loyalty_input)

