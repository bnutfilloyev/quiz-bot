from aiogram import types

from keyboards.poll_keyboard import remove_keyboard
from loader import dp


@dp.message_handler(text="Отмена")
async def action_cancel(message: types.Message):
    await message.answer("Действие отменено. Введите /start, чтобы начать заново.", reply_markup=remove_keyboard)