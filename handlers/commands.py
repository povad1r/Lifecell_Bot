import os
from datetime import datetime
from random import choice

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from create_bot import dp, bot, db

from keyboards import start_kb
from keyboards.start_kb import new_captcha_kb_func
from states import choose_tariff

from captcha.image import ImageCaptcha

from states.choose_tariff import Captcha


# КОМАНДА /START
async def start(message: Message, state: FSMContext):
    if message.chat.id == message.from_user.id:

        user_id = message.from_user.id
        photo = open('static/lifecell.gif', 'rb')

        if await db.sql_get_user_id(user_id):
            await bot.send_animation(chat_id=message.chat.id,
                                     animation=photo,
                                     caption=f'<b>👋 Привіт!\n➖➖➖➖➖➖➖➖➖➖➖\n'
                                             f'📈 Цей бот допоможе тобі обрати вигідний тариф компанії «Lifecell»</b>',
                                     reply_markup=await start_kb.choose_order_kb_func(),
                                     parse_mode='HTML')
        else:
            await Captcha.captcha_input.set()

            captcha_text, captcha_msg = await captcha_create(message=message)
            async with state.proxy() as data:
                data['captcha_text'] = captcha_text
                data['old_captcha_id'] = captcha_msg.message_id


async def new_captcha(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        try:
            await bot.delete_message(chat_id=call.message.chat.id, message_id=data['old_captcha_id'])
        except:
            pass
    captcha_text, captcha_msg = await captcha_create(message=call.message)
    async with state.proxy() as data:
        data['captcha_text'] = captcha_text
        data['old_captcha_id'] = captcha_msg.message_id


async def captcha_input(message: Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == data['captcha_text']:
            try:
                await bot.edit_message_reply_markup(chat_id=message.chat.id,
                                                    message_id=data['old_captcha_id'],
                                                    reply_markup=None)
            except:
                pass

            await db.sql_create_user(user_id=message.from_user.id,
                                     datetime=str(datetime.now()))

            await message.answer(text='<b>Вы успішно верифікувалися!</b>',
                                 parse_mode='HTML')

            photo = open('static/lifecell.gif', 'rb')
            await bot.send_animation(chat_id=message.chat.id,
                                     animation=photo,
                                     caption=f'<b>👋 Привіт!\n➖➖➖➖➖➖➖➖➖➖➖\n'
                                             f'📈 Цей бот допоможе тобі обрати вигідний тариф компанії «Lifecell»</b>',
                                     reply_markup=await start_kb.choose_order_kb_func(),
                                     parse_mode='HTML')

            await state.finish()
        else:
            await message.answer(text='*Не вірно!\n\n🔄 Спробуйте ще раз:*',
                                 parse_mode='Markdown')


async def captcha_create(message):
    symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5',
               '6', '7',
               '8', '9']

    pattern = []
    captcha_text = ''
    for i in range(5):
        pattern.append(choice(symbols))
        captcha_text += pattern[i]

    image_captcha = ImageCaptcha(width=320, height=200)
    image_captcha.write(pattern, f'captcha/{message.from_user.id}.png')

    captcha_photo = open(f'captcha/{message.from_user.id}.png', 'rb')

    captcha_msg = await bot.send_photo(chat_id=message.chat.id,
                                       photo=captcha_photo,
                                       caption='<b>Будь ласка, пройдіть капчу.\n✍ Вкажіть цифри з картинки:</b>',
                                       reply_markup=await new_captcha_kb_func(),
                                       parse_mode='HTML')

    os.remove(f'captcha/{message.from_user.id}.png')

    return captcha_text, captcha_msg


async def tariff_order(call: CallbackQuery):
    try:
        await bot.delete_message(chat_id=call,
                                 message_id=call.message.message_id)
    except:
        pass
    await choose_tariff.ChooseTariff.price_input.set()


@dp.callback_query_handler(text='🗑 Закрити', state='*')
async def close(call: CallbackQuery):
    await call.answer(text='Меню приховано!')

    try:
        await bot.delete_message(chat_id=call.message.chat.id,
                                 message_id=call.message.message_id)
    except:
        pass


def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(start, Command('start'))
    dp.register_message_handler(captcha_input, state=Captcha.captcha_input)
    dp.register_callback_query_handler(new_captcha, lambda c: c.data and c.data.startswith('new_captcha:'),
                                       state=Captcha.captcha_input)
    dp.register_callback_query_handler(close, text='close:', state='*')
    dp.register_callback_query_handler(tariff_order, text='choose_order:', state='*')
