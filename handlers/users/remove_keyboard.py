from aiogram import types
from aiogram.dispatcher import FSMContext

from data.text import button_text, text
from keyboards.poll_keyboard import remove_keyboard
from loader import dp


@dp.message_handler(text=button_text['cancel_button'], state="*")
async def action_cancel(message: types.Message, state: FSMContext):
    await message.answer(text['get_quiz_stoped'], reply_markup=remove_keyboard)
    await state.finish()