import os
from utils.sheet_connect import get_stat
from utils.sheet_connect import get_level
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token=os.environ["TOKEN"])
dp = Dispatcher(bot)

names = {
    "orloffdd": "Орлов Даниил",
    "kill_your_soul": "Платонов Дмитрий",
    "klafuty": "Клешкова Алисия",
}


@dp.message_handler(commands=["start"])
async def command_start(message: types.Message):
    await message.answer(
        'Привет! Я - бот, призванный сделать процесс твоего поиска интереснее и веселее. Давай начнем! Напиши мне "Статистика"'
    )


@dp.message_handler(text="Статистика")
async def stat_send(message: types.Message):
    msg = await message.answer("Запрос обрабатывается, подожди...")
    stat = await get_stat(names.get(message.from_user.username), "stat")
    await msg.edit_text(stat)
    # await message.answer(stat[1])


@dp.message_handler(text="Посмотреть уровень")
async def lvl_send(message: types.Message):
    msg = await message.answer("Запрос обрабатывается, подожди...")
    lvl = await get_level(names.get(message.from_user.username))
    await msg.edit_text(lvl)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
