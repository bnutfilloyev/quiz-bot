from aiogram.types import CallbackQuery

from keyboards.inline.callback_data import subject_callback
from loader import dp


@dp.callback_query_handler(text_contains='subject')
async def choose_subject(call: CallbackQuery):
    await call.message.edit_text()