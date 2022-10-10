import os
import asyncio
from utils.sheet_connect import *
from utils.printFunc import *
from buttons.but import keybrd
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from utils.person import Person


storage = MemoryStorage()

bot = Bot(token=os.environ["TOKEN"])
dp = Dispatcher(bot, storage=storage)

names = {
    "orloffdd": "Орлов Даниил",
    "kill_your_soul": "Платонов Дмитрий",
    "klafuty": "Клешкова Алисия",
}


@dp.message_handler(commands=["start"])
async def command_start(message: types.Message, state: FSMContext):

    name = names.get(message.from_user.username)
    await message.answer(
        "Привет! Я - бот, призванный сделать процесс твоего поиска интереснее и веселее. Давай начнем! Учти, что бот обновляет базу каждые 5 минут😉",
        reply_markup=keybrd,
    )

    stat = await get_stat(name)
    async with state.proxy() as data:
        data["person"] = Person(
            stat[0], stat[1], stat[2], stat[3], stat[4], stat[5], stat[6]
        )

        enemies = await get_enemy(data["person"])
        data["min_enemy"] = Person(
            enemies[0][0], enemies[0][1], enemies[0][2], enemies[0][3], "", "", ""
        )

        data["max_enemy"] = Person(
            enemies[1][0], enemies[1][1], enemies[1][2], enemies[1][3], "", "", ""
        )

    global stop_polling_sheet
    stop_polling_sheet = asyncio.Event()
    while True:
        try:
            await asyncio.wait_for(stop_polling_sheet.wait(), timeout=300)
        except asyncio.TimeoutError:
            try:
                stat = await get_stat(name)
                async with state.proxy() as data:
                    data["person"] = Person(
                        stat[0], stat[1], stat[2], stat[3], stat[4], stat[5], stat[6]
                    )

                    enemies = await get_enemy(data["person"])
                    data["min_enemy"] = Person(
                        enemies[0][0],
                        enemies[0][1],
                        enemies[0][2],
                        enemies[0][3],
                        "",
                        "",
                        "",
                    )

                    data["max_enemy"] = Person(
                        enemies[1][0],
                        enemies[1][1],
                        enemies[1][2],
                        enemies[1][3],
                        "",
                        "",
                        "",
                    )

            except:
                print("not working")


@dp.message_handler(text="📈Статистика")
async def stat_send(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        stat = await print_stat(data["person"])
        await message.answer(stat)


@dp.message_handler(text="🏆Уровень")
async def lvl_send(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        lvl = await print_lvl(data["person"])
        await message.answer(lvl)


@dp.message_handler(text="Соседние результаты")
async def send_enemy(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        enemy = await enemies_print(data["min_enemy"], data["max_enemy"])
        try:
            await message.answer(enemy[0])
        except:
            pass

        try:
            await message.answer(enemy[1])
        except:
            pass


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
