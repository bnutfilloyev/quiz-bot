from aiogram import types

from data.text import text
from keyboards.poll_keyboard import poll_keyboard
from loader import dp


@dp.message_handler(commands=["add_quiz"])
async def cmd_start(message: types.Message):
    awa
    # await message.answer(text=text['create_quiz_hello'], reply_markup=poll_keyboard)
