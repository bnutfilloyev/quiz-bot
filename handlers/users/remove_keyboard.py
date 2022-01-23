from aiogram import types

from data.text import button_text, text
from keyboards.poll_keyboard import remove_keyboard
from loader import dp


@dp.message_handler(text=button_text['cancel_button'])
async def action_cancel(message: types.Message):
    await message.answer(text['get_quiz_stoped'], reply_markup=remove_keyboard)
