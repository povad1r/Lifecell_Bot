from aiogram import executor

from create_bot import dp, db
from handlers import commands

commands.register_handlers_commands(dp)


async def on_startup(_):
    await db.bd_start()

if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup)
