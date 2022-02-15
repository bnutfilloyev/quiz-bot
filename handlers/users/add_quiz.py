from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from data.text import text
from keyboards.inline.choose_subject import Subject, Curriculum, Level
from keyboards.poll_keyboard import poll_keyboard
from loader import dp
from states.States import Form


@dp.message_handler(commands=["add_quiz"], state="*")
async def cmd_start(msg: types.Message):
    await Form.addPoll.set()
    await msg.answer(text['inline_text'], reply_markup=Subject)


@dp.callback_query_handler(text_contains='subject', state=Form.addPoll)
async def choose_curriculum(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        split_data = call.data.split(':')
        data[split_data[0]] = split_data[-1]
        await call.message.edit_text(text['inline_text'], reply_markup=Curriculum)


@dp.callback_query_handler(text_contains='curriculum', state=Form.addPoll)
async def choose_level(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        split_data = call.data.split(':')
        data[split_data[0]] = split_data[-1]
        await call.message.edit_text(text['inline_text'], reply_markup=Level)


@dp.callback_query_handler(text_contains='level', state=Form.addPoll)
async def choose_level(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        split_data = call.data.split(':')
        data[split_data[0]] = split_data[-1]
        await call.message.answer(text=text['create_quiz_hello'], reply_markup=poll_keyboard)
    # await state.finish()

