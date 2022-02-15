from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from data.text import text, button_text
from keyboards.inline.choose_subject import Curriculum, Level, Subject
from loader import dp


@dp.message_handler(text=button_text['solve_test_text'], state="*")
async def choose_subject(msg: types.Message):
    await msg.answer(text['inline_text'], reply_markup=Subject)


@dp.callback_query_handler(text_contains='subject')
async def choose_curriculum(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        split_data = call.data.split(':')
        data[split_data[0]] = split_data[-1]
        await call.message.edit_text(text['inline_text'], reply_markup=Curriculum)


@dp.callback_query_handler(text_contains='curriculum')
async def choose_level(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        split_data = call.data.split(':')
        data[split_data[0]] = split_data[-1]
        await call.message.edit_text(text['inline_text'], reply_markup=Level)
