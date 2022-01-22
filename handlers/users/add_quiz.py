from aiogram import types

from data import text
from keyboards.poll_keyboard import poll_keyboard
from loader import dp, bot


@dp.message_handler(commands=["add_quiz"])
async def cmd_start(message: types.Message):
    await message.answer(text=text['create_quiz_hello'], reply_markup=poll_keyboard)

