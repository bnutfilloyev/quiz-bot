from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.text import text
from keyboards.default.menuKeyboard import menu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(text=text['start_text'].format(message.from_user.full_name), reply_markup=menu)