import asyncio

from random import randint
from aiogram import Bot, Dispatcher, executor, types
from constants import TOKEN_API, keyb_start, keyb_timer, keyb_cancel, keyb_dice

bot = Bot(TOKEN_API)
dispatch = Dispatcher(bot)

dictionary = {}


@dispatch.message_handler(commands=["start"])
async def start_message(message: types.Message):
    await bot.send_message(text="Выберите желаемое действие", reply_markup=keyb_start, chat_id=message.from_user.id)


@dispatch.message_handler(commands=["timer"])
async def set_timer(message: types.Message):
    await bot.send_message(text="Выберите время", reply_markup=keyb_timer, chat_id=message.from_user.id)
    await message.delete()


@dispatch.message_handler(commands=["back"])
async def set_timer(message: types.Message):
    await message.delete()
    await bot.send_message(text="Выберите действие", reply_markup=keyb_start, chat_id=message.from_user.id)


@dispatch.message_handler(commands=["dice"])
async def help_message(message: types.Message):
    await message.delete()
    await bot.send_message(text="Выберите действие", reply_markup=keyb_dice, chat_id=message.from_user.id)


@dispatch.message_handler(commands=["close"])
async def help_message(message: types.Message):
    await message.delete()

    dictionary[message.from_user.id] = 0


@dispatch.message_handler(commands=["set_30_seconds", "set_1_minute", "set_5_minutes"])
async def timer(message: types.Message):
    await message.delete()
    dictionary[message.from_user.id] = -1

    if message.text == "/set_30_seconds":
        dictionary[message.from_user.id] = 30

    elif message.text == "/set_1_minute":
        dictionary[message.from_user.id] = 60

    elif message.text == "/set_5_minutes":
        dictionary[message.from_user.id] = 300

    if dictionary[message.from_user.id] != -1:
        string_n = dictionary[message.from_user.id]

        await message.answer(
            text=f"Засёк {str(dictionary[message.from_user.id] // 60) + ' мин.' if dictionary[message.from_user.id] >= 60 else ''}{str(dictionary[message.from_user.id]) + ' сек.' if dictionary[message.from_user.id] == 30 else ''}",
            reply_markup=keyb_cancel)

        while dictionary[message.from_user.id] > 0:
            dictionary[message.from_user.id] -= 1
            await asyncio.sleep(1)

        await bot.send_message(text=f"Время {string_n} cек. истекло", reply_markup=keyb_timer,
                               chat_id=message.from_user.id)


@dispatch.message_handler(commands=["roll_one_hexagon_dice", "roll_two_hexagon_dice", "roll_the_20-sided_dice"])
async def timer(message: types.Message):
    await message.delete()
    if message.text == "/roll_one_hexagon_dice":
        await bot.send_message(text=f"{randint(1, 6)}", chat_id=message.from_user.id)

    elif message.text == "/roll_two_hexagon_dice":
        await bot.send_message(text=f"{randint(1, 6)} {randint(1, 6)}", chat_id=message.from_user.id)

    elif message.text == "/roll_the_20-sided_dice":
        await bot.send_message(text=f"{randint(1, 20)}", chat_id=message.from_user.id)


if __name__ == "__main__":
    executor.start_polling(dispatcher=dispatch, skip_updates=True)
